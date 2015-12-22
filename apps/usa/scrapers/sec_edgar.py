# -*- coding: utf-8 -*-
"""
Securities and Exchange Commission Edgar Dataset  Scraper

This dataset contains regulatory filings from publicly
traded US corporations.

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
import itertools
import datetime as dt

from apps.corex.basescraper import BaseScraper
from apps.corex.utils import auto_retry
from ..models import FedSecFiling

# ============================================================================
# useful constants
# ============================================================================
FTP_URL = 'ftp://ftp.sec.gov/edgar/full-index/{}/form.gz'
TXT_URL = 'http://www.sec.gov/Archives/{}'
YEARS = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
QTRS = ['QTR1', 'QTR2', 'QTR3', 'QTR4']


# ============================================================================
# scraper implementation
# ============================================================================
class SecEdgarScraper(BaseScraper):
    """SEC Edgar database scraper"""
    NAME = 'usa:sec-edgar'

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    @auto_retry(exc=IOError)
    def download_form(self, url):
        """download form file from url"""
        form = self.download_ftp(url, gzp=True)

        return form

    def download_forms(self, urls):
        """download form files from urls"""
        for url in urls:
            yield self.download_form(url)

    def download_txts(self, urls):
        """download txt files from urls as beautiful soup objs"""
        for url in urls:
            yield (self.get_soup(url), url)

    def fetch_data(self):
        """fetch data from SEC site"""
        for form in self.download_forms(self.gen_ftp_urls()):
            for data in self.scrape_data(self.download_txts(self.gen_txt_urls(form))):
                yield data

    @staticmethod
    def gen_ftp_urls():
        """generate ftp urls"""
        for epoc in itertools.product(YEARS, QTRS):
            url = FTP_URL.format('{}/{}'.format(epoc[0], epoc[1]))
            yield url

    @staticmethod
    def gen_txt_urls(form):
        """generate txt urls from form file"""
        for line in form:
            path = line.strip().split(' ')[-1]
            if path.endswith('.txt'):
                url = TXT_URL.format(path)
                yield url

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            model = FedSecFiling(**data)
            self.save_model(model)

            yield

    def scrape_data(self, soups):
        """scrape data from soups"""
        for soup, url in soups:
            yield self.scrape_datum(soup, url)

    def scrape_datum(self, soup, url):
        """scrape data from soup"""
        paper = soup.find('paper')
        if not paper:
            paper = soup.find('acceptance-datetime')

        lines = [x.strip() for x in paper.text.split('\n') if x.strip()]
        data = [x.split(':')[:2] for x in lines if len(x.split(':')) > 1]
        try:
            data = dict([(x.lower().strip().replace(' ', '_'), y) for x, y in data])
        except ValueError as err:
            raise err

        for key, val in data.items():
            data[key] = val.replace('\t', '')

        data['url'] = url
        data['filed_as_of_date'] = dt.datetime.strptime(data['filed_as_of_date'], "%Y%m%d").date()
        data['hash'] = self.get_hash(data)

        return data

# ============================================================================
# EOF
# ============================================================================
