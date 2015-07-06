# -*- coding: utf-8 -*-
"""
Serbia's Public Officials Scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = April 2015

"""
# ============================================================================
# Make necessary imports
# ============================================================================
import re
import copy
import datetime

from django.db.utils import IntegrityError

from corex.basescraper import BaseScraper
from .. import models


# ============================================================================
# Define constants
# ============================================================================
SEARCH_URL = 'http://www.acas.rs/acasPublic/imovinaFunkcioneraSearch.htm'
DATA_URL = 'http://www.acas.rs/acasPublic/izvestajDetails.htm?parent=pretragaIzvestaja&izvestajId={}'


# ============================================================================
# Define scraper
# ============================================================================
class SerbiaOfficialsScraper(BaseScraper):
    """Serbian Public Officials Scraper """
    def __init__(self):
        """Initialize scraper"""
        BaseScraper.__init__(self)

    def extract_date(self, soup):
        """Extract date from soup"""
        header = ['_', 'date']

        date = self.extract_entities(header, -1, soup)[0]

        date = date['date'].split(',')[1].strip()

        date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

        return date

    @staticmethod
    def extract_deposits(soup):
        """extract deposits info from soup"""
        tab = soup.find_all('table', {'class': 'table1'})[5]
        rows = tab.find('tbody').find_all('tr')

        if rows[-1].find('img'):
            return False

        return True

    @staticmethod
    def extract_entities(headers, tab_idx, soup):
        """Extract entities"""
        entities = []
        tab = soup.find_all('table', {'class': 'table1'})[tab_idx]
        rows = tab.find('tbody').find_all('tr')

        for row in rows:
            data = [cell.text.strip() for cell in row.find_all('td')]
            if data[0] == u'-':
                try:
                    data[0] = entities[0][headers[0]]
                except IndexError:
                    pass
            entities.append(dict(zip(headers, data)))

        return entities

    def extract_fassets(self, soup):
        """Extract fixed assets info from soup"""
        hdrs = ['type_size', 'ownership_stake', 'acquisition_basis']

        assets = self.extract_entities(hdrs, 3, soup)

        return assets

    def extract_flats(self, soup):
        """Extract flats info from soup"""
        hdrs = ['place', 'structure', 'allocation_basis', 'closing_date']

        flats = self.extract_entities(hdrs, 6, soup)

        return flats

    @staticmethod
    def extract_name(soup):
        """Extract name from soup"""
        name_tab = soup.find_all('table', {'class': 'table1'})[1]
        name = name_tab.find('td', {'class': 'tdCell'}).text.strip()

        return name

    def extract_place(self, soup):
        """Extract place from soup"""
        hdr = ['_', 'place']

        place = self.extract_entities(hdr, -1, soup)[0]

        place = place['place'].split(',')[0]

        return place

    def extract_revenues(self, soup):
        """Extract revenues from soup"""
        hdrs = ['position', 'authority', 'income_source', 'interval',
                'net_income', 'currency', 'time_period']

        revenues = self.extract_entities(hdrs, 2, soup)

        return revenues

    def extract_transports(self, soup):
        """Extract transports from soup"""
        hdrs = ['type', 'brand', 'year', 'acquisition_basis']

        transports = self.extract_entities(hdrs, 4, soup)

        return transports

    def get_json_data(self):
        """fetch json data """
        cookies = {
            'pll_language': 'en',
            'stl_default_lang': 'cir',
            'em_transient_id': 'emtr_165d7f9a629e4563110b06dcbe91b5b744d1d120'}

        headers = {
            'Accept': 'application/json, text/javascript, */*',
            'Content-Length': 118,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.acas.rs',
            'Origin': 'http://www.acas.rs',
            'Referer': 'http://www.acas.rs/acasPublic/imovinaFunkcioneraSearch.htm',
            'X-Requested-With': 'XMLHttpRequest'}

        payload = {'sEcho': 3, 'iColumns': 3, 'sColumns': '',
                   'iDisplayStart': 0, 'iDisplayLength': 100,
                   'mDataProp_0': 0, 'mDataProp_1': 1,
                   'mDataProp_2': 2, 'prezime': '', 'ime': ''}

        self.session.headers.update(headers)

        for interval in range(0, 16000, 100):
            payload['iDisplayStart'] = interval

            res = self.post(SEARCH_URL, data=payload, cookies=cookies)

            yield res.json()

    def make_model(self, model, data, lst=True):
        """make db model instance(s)"""
        def _make_model(dat):
            """make model"""
            dat[u'hash'] = self.get_hash(dat)
            mod = model(**dat)
            return mod

        if not lst:
            return _make_model(data)

        mods = [_make_model(d) for d in data]

        return mods

    def run(self):
        """run scraper"""

        offs = (self.scrape_url(url)
                for url in self.yield_data_urls(self.get_json_data()))

        for off in offs:
            official = copy.deepcopy(off)

            for key in ['flats', 'revenues', 'fixed_assets', 'transports']:
                official.pop(key)

            official = self.make_model(models.Official, official, lst=False)

            official = self.save_model(official)

            if not official:
                continue

            for key in ['flats', 'revenues', 'fixed_assets', 'transports']:
                for item in off[key]:
                    item['official'] = official

            est = self.make_model(models.RealEstate, off['flats'])
            sal = self.make_model(models.Salary, off['revenues'])
            asst = self.make_model(models.FixedAsset, off['fixed_assets'])
            trp = self.make_model(models.Transport, off['transports'])

            for mod in self.utils.flatten_list([est, sal, asst, trp]):
                self.save_model(mod)

            yield

    def save_model(self, model, report_error=True):
        """save model to database"""
        try:
            super(SerbiaOfficialsScraper, self).save_model(model, report_error)
            return model
        except IntegrityError:
            return None

    def scrape_url(self, url):
        """scrape url

        self.scrape_url(url) -> result_dict

        """
        soup = self.get_soup_basic(url)

        res = {}
        res['url'] = url
        res['name'] = self.extract_name(soup)
        res['revenues'] = self.extract_revenues(soup)
        res['fixed_assets'] = self.extract_fassets(soup)
        res['transports'] = self.extract_transports(soup)
        res['deposits_savings'] = self.extract_deposits(soup)
        res['flats'] = self.extract_flats(soup)
        res['place'] = self.extract_place(soup)
        res['date'] = self.extract_date(soup)
        res['year'] = res['date'].year
        res['title'] = ', '.join(set([x['position'] for x in res['revenues']]))

        return res

    @staticmethod
    def yield_data_urls(json_gen):
        """parse json data for ids and generate data urls based on ids"""
        URLS = [off.url for off in models.Official.objects.all()]
        for json in json_gen:
            for data in json[u'aaData']:
                idx = re.findall('\\d+', data[2].split(';', 1)[0])[0]
                url = DATA_URL.format(idx)
                if url in URLS:
                    continue
                yield url


if __name__ == '__main__':
    pass
# ============================================================================
# EOF
# ============================================================================
