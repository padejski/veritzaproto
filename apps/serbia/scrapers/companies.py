# -*- coding: utf-8 -*-
"""
Serbia's Company Registry Scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = April 2015

"""

# ============================================================================
# Make necessary imports
# ============================================================================
import os
import time
import datetime
from itertools import chain

from bs4 import BeautifulSoup as bs

from apps.corex.basescraper import BaseScraper
from ..models import Company


# ============================================================================
# Define Constants
# ============================================================================
BASE_URL = 'http://pretraga2.apr.gov.rs'
START_URL = 'http://pretraga2.apr.gov.rs/ObjedinjenePretrage/Search/Search'
POST_URL = 'http://pretraga2.apr.gov.rs/ObjedinjenePretrage/Search/SearchResult'

EXTRA_LINKS = [u'Управни одбор', u'Надзорни одбор', u'Остали заступници',
               u'Законски заступници', u'Чланови', u'Пословни подаци']
HEADERS = [u'Седиште', u'Матични број', u'Пословно Име', u'Назив',
           u'Скраћено пословно име', u'Статус', u'Датум брисања',
           u'Датум оснивања', u'ПИБ', u'Правна форма', u'Име Презиме',
           u'Функција', u'Самостално заступа', u'Тип', u'Удео']

MAPPING = [(u'Седиште', 'city'),
           (u'Пословно име', 'name'),
           (u'Јмбг/Лични број', 'founder_number'),
           (u'Име Презиме', 'founders'),
           (u'Матични број', 'company_id'),
           (u'Скраћено пословно име', 'alt_name'),
           (u'Статус', 'status'),
           (u'Датум брисања', 'termination_date'),
           (u'Датум оснивања', 'reg_date'),
           (u'ПИБ', 'tax_number'),
           (u'Правна форма', 'type'),
           (u'Назив делатности', 'industry'),
           ('directors', 'directors'),
           ('legal_rep', 'legal_rep'),
           ('members', 'members'),
           ('supervisors', 'supervisors'),
           ('other_individuals', 'other_individuals')]

CODES_FILE = 'IDS3.csv'


# ============================================================================
# Company Scraper
# ============================================================================
class SerbiaCompanyScraper(BaseScraper):
    """Serbian Business Registry Scraper"""
    NAME = 'serbia:companies'

    def __init__(self):
        """Initialize scraper """
        BaseScraper.__init__(self)

    @staticmethod
    def dkey_to_dict(old_dict, old_key, new_key):
        """extract key from dictionary and return it in a new dictionary
        with a different name.
        """
        try:
            return {new_key: old_dict[old_key]}
        except KeyError:
            return {}

    def extract_xtra_urls(self, url):
        """extract extra information urls"""
        soup = self.get_soup(url)
        anchors = soup.find('ul', {'id': 'navlist'}).find_all('a')

        xtra_urls = []

        for link in EXTRA_LINKS:
            for anchor in anchors:
                if link in ' '.join([x.strip() for x in anchor.text.split('\n')]):
                    url = BASE_URL + anchor.get('href')
                    xtra_urls.append(url)

        return xtra_urls

    @staticmethod
    def fetch_codes(dfile):
        """
        Fetch unique numeric identifier from file.

        Read and return elements of the second column of the dfile csv.

        args:
            dfile (str): file path

        returns:
            codes (genexp): generator expression of codes

        """
        try:
            codes = (line.split(',')[1] for line in open(dfile, 'r'))

            next(codes)  # remove header row
        except IndexError:
            codes = (line.strip() for line in open(dfile))

        return codes

    def fetch_url(self, code):
        """
        Extract url to information page from initial webpage

        """
        vtoken = bs(self.get(START_URL).text).find('input', {'type': 'hidden'}).get('value')

        formdata = {'__RequestVerificationToken': vtoken,
                    'rdbtnSelectInputType': 'mbr',
                    'SearchByRegistryCodeString': code,
                    'X-Requested-With': 'XMLHttpRequest'}

        try:
            url = bs(self.post(POST_URL, data=formdata).text).find('a').get('href')
        except AttributeError:
            url = None

        return url

    def generate_codes(self, dfile):
        """
        Yield unique identifier codes for the pretraga search page

        args:
            dfile (str): path to csv file containing unique numeric identifiers

        yields:
            code (str): an 8-digit numeric identifier

        """
        # codes = [int(x) for x in self.fetch_codes(dfile)]
        # codes = (str(x) for x in xrange(min(codes), max(codes)))
        codes = (x for x in self.fetch_codes(dfile))

        for code in codes:
            if len(code) == 7:
                code = '0' + code
            yield code

    @staticmethod
    def generate_csv(headers, data):
        """Generate csv file

        args:
            headers (list): csv headers
            data (dict): dict with keys matching the csv headers

        yields:
            row (str): csv row

        """

        yield ','.join(headers + ['\n'])

        for dic in data:
            row = ','.join([dic.get(x, 'NA').replace(',', '')
                            for x in headers]) + '\n'

            yield row

    def generate_urls(self, codes):
        """Generate info links unique identifier codes

        Search each code on the pretraga search page and get the
        info link from the search results

        args:
            codes (iterable): list of codes

        yields:
            url (str): url

        """
        ids = [obj.company_id for obj in Company.objects.all()]

        for code in codes:
            if code in ids:
                continue
            url = self.fetch_url(code)

            if url:
                yield url

    def scrape_info(self, url):
        """scrape info from url"""
        content_dict = self.scrape_url(url)
        extra_urls = self.extract_xtra_urls(url)
        extra_info = (self.scrape_url(url) for url in extra_urls)

        for info in extra_info:
            content_dict.update(info)

        ret = {}

        for serb, eng in MAPPING:
            try:
                ret[eng] = content_dict[serb]
            except KeyError:
                continue

        ret['url'] = START_URL
        ret['reg_date'] = datetime.datetime.strptime(ret['reg_date'], "%d.%m.%Y").date()

        ret[u'area'], ret[u'place'], ret[u'address'] = [
            x.split(':')[1] for x in ret['city'].split('|')]

        del ret['city']

        ret[u'hash'] = self.get_hash(ret)

        return ret

    def scrape_url(self, url):
        """Scrape info from url

        scrape_link(url) -> dict

        args:
            url (str): url

        returns:
            content_dict (dict): dict with scraped info

        """
        try:
            soup = self.get_soup(url)
            content = [x.find_all('p') for x in
                       soup.find_all('div', {'class': 'GroupContent'}) if x.find('p')]
            content = self.utils.flatten_list(content)

            content = chain.from_iterable([x.text.split('\r\n') for x in content])

            content = [x.split(':', 1) for x in content if
                       len(x.split(':', 1)) == 2]

            cdict = {k.strip(): v.strip() for k, v in content}

            if 'legaltrust' in url.lower():
                cdict = self.dkey_to_dict(cdict, u'Име Презиме', 'legal_rep')

            if 'enterprisesteeri' in url.lower():
                cdict = self.dkey_to_dict(cdict, u'Име Презиме', 'directors')

            if 'enterprisemember' in url.lower():
                cdict = self.dkey_to_dict(cdict, u'Име Презиме', 'members')

            if 'supervisoryboard' in url.lower():
                cdict = self.dkey_to_dict(cdict, u'Име Презиме', 'supervisors')

            if 'othertrustees' in url.lower():
                cdict = self.dkey_to_dict(cdict, u'Име Презиме', 'other_individuals')
        except AttributeError:
            cdict = {}

        return cdict

    def run(self):
        """execute scraping routine"""

        # company codes file
        cfile = os.path.dirname(os.path.abspath(__file__)) + '/' + CODES_FILE

        # fetch companies data urls using codes
        urls = self.generate_urls(self.generate_codes(cfile))

        data = (self.scrape_info(url) for url in urls)

        # save data to database
        for dat in data:
            time.sleep(10)  # time delay to avoid ip banning
            if dat:
                model = Company(**dat)
                self.save_model(model)

                yield  # scraper's cooperative multitasking hook


# ============================================================================
# Execute program
# ============================================================================
if __name__ == '__main__':
    pass
# ============================================================================
# EOF
# ============================================================================
