# -*- coding: utf-8 -*-
"""
Serbia's Public Procurement scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = May 2015

"""
# ============================================================================
# Make necessary imports
# ============================================================================
from itertools import imap

from django.db.utils import IntegrityError

from corex.basescraper import BaseScraper
from ..models import Procurement


# ============================================================================
# Define constants
# ============================================================================
BASE_URL = 'http://portal.ujn.gov.rs/Izvestaji/IzvestajiVelike.aspx'
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140610 "
MAX_PAGE = 100
HEADERS = [
    'contracting_auth',
    'contracting_auth_id',
    'contracting_auth_address',
    'place',
    'supplier_name',
    'supplier_id',
    'supplier_country',
    'procedure_type',
    'ppo_reviews',
    'lpp_basis',
    'orn_code',
    'cases_types',
    'subject',
    'desc',
    'date',
    'purchases_val_estimate',
    'purchases_val_contract',
    'price',
    'offers',
    'selection_criterion',
    'eq_price',
    'preparing_bids_cost',
    'execution_date',
    'execution_value',
    'execution_note',
    'default_reason',
    'type',
    'modifications'
]


# ============================================================================
# Procurement scraper class
# ============================================================================
class SerbiaProcurementScraper(BaseScraper):
    """Serbia Procurement Scraper """
    def __init__(self):
        """initialize base class"""
        BaseScraper.__init__(self)

    def _gen_data_dicts(self, soup):
        """scrape data from soup as dictionaries"""
        for row in self.scrape_data_rows(soup):
            data_dict = dict(zip(HEADERS, row))

            if len(data_dict.keys()) != len(HEADERS):
                continue

            data_dict['url'] = BASE_URL
            data_dict['execution_date'] = \
                self.str2date(data_dict['execution_date'].strip(), "%Y-%m-%d")
            data_dict['date'] = \
                self.str2date(data_dict['date'].strip(), "%Y-%m-%d")
            data_dict['hash'] = self.get_hash(data_dict)

            yield data_dict

    def gen_data_dicts(self):
        """generate scraped data as dictionaries """
        for soup in self.gen_page_soup():
            for data_dict in self._gen_data_dicts(soup):
                yield data_dict

    def gen_models(self, data_dicts):
        """generate procurement database models from data dicts"""
        for model in imap(self.make_model, data_dicts):
            yield model

    def gen_page_soup(self):
        """generate page soups"""
        for page in range(1, MAX_PAGE):
            yield self.get_page_soup(page)

    def get_page_soup(self, page):
        """Get paginated page as beautiful soup

        get_page_soup(page_number_int) -> soup

        args:
            page (int): page number

        returns:
            soup (obj): BeautifulSoup instance

        """
        self.session.get(BASE_URL)

        page = 'Page${}'.format(page)

        payload = {
            '__EVENTTARGET': 'ctl00$cphMain$gvIzvestaji',
            '__EVENTARGUMENT': page,
            '__LASTFOCUS': '',
            '__VIEWSTATE': self.get_viewstate_value(),
            '__VIEWSTATEENCRYPTED': '',
            'ctl00$cphMain$gvIzvestaji$ctl16$btnIzmene': ''
        }

        soup = self.post_soup(BASE_URL, data=payload)

        return soup

    def get_viewstate_value(self):
        """fetch view state value"""
        soup = self.get_soup(BASE_URL)
        val = soup.find('input', {'name': '__VIEWSTATE'}).get('value')

        return val

    @staticmethod
    def make_model(data_dict):
        """make procurement database model from data dictionary """
        model = Procurement(**data_dict)

        return model

    def run(self):
        """run scraper"""
        for model in self.gen_models(self.gen_data_dicts()):
            self.save_model(model)
            yield

    @staticmethod
    def scrape_data_rows(soup):
        """get data rows from soup"""
        soup = soup.find('table', {'id': 'ctl00_cphMain_gvIzvestaji'})

        for row in soup.find_all('tr')[1:]:
            row = [cell.text for cell in row.find_all('td')]
            yield row

    @staticmethod
    def scrape_headers(soup):
        """get data headers from soup"""
        soup = soup.find('tr', {'class': 'GridHeaderWithoutFilter alignCenter'})
        headers = [th.text for th in soup.find_all('th')]

        return headers


if __name__ == '__main__':
    pass
