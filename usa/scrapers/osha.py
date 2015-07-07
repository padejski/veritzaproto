# -*- coding: utf-8 -*-
"""
OSHA WOrkplace Safety Data Scrapers

http://ogesdw.dol.gov/views/data_catalogs.php

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
from corex.basescraper import BaseScraper
from ..models import FedOshaEbsa, FedOshaInspection

# ============================================================================
# useful constants
# ============================================================================
BASE_URL = 'http://ogesdw.dol.gov/views/data_summary.php'
EBSA_HEADERS = ['case_type', 'ein', 'pn', 'plan_year', 'plan_name', 'plan_admin',
                'plan_admin_state', 'plan_admin_zip_code', 'final_close_reason',
                'final_close_date', 'penalty_amount']


# ============================================================================
# scrapers implementation
# ============================================================================
class OshaEbsaScraper(BaseScraper):
    """OSHA EBSA Enforcement data scraper"""

    def __init__(self):
        """init base class"""
        BaseScraper.__init__(self)

    def download_file(self):
        """download and deflate zip data file"""
        ebsa_url = self.get_ebsa_url()
        print(ebsa_url)
        zfile = self.download_http(ebsa_url, zfile=True)

        return zfile.open('ebsa_ocats.csv')

    def fetch_data(self):
        """fetch data from OSHA site"""
        for data in self.gen_data_dicts(self.download_file()):
            yield data

    def gen_data_dicts(self, dfile):
        """generate data dictionaries

        args:
            dfile: data csv file

        yields:
            data (dict): data dictionary

        """
        lines = (line.split(',') for line in dfile)

        # discard csv headers
        next(lines)

        for line in lines:
            data = dict(zip(EBSA_HEADERS, line))
            data['hash'] = self.get_hash(data)

            yield data

    def get_ebsa_url(self):
        """. """
        self.session.get(BASE_URL)

        payload = {'agency': 'ebsa'}

        soup = self.post_soup(BASE_URL, data=payload)
        url = [a.get('href') for a in
               soup.find('table', {'class': 'download-table'}).find_all('a')
               if 'ebsa_ocats' in a.get('href')][0]

        url = url.replace('../', '')

        return url

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            data = FedOshaEbsa(**data)
            self.save_model(data)

            yield


class OshaInspectionScraper(BaseScraper):
    """OSHA Inspection data scraper"""

    def __init__(self):
        """init base class"""
        BaseScraper.__init__(self)

    def download_file(self):
        """download and deflate zip data file"""
        insp_url = self.get_insp_url()
        zfile = self.download_http(insp_url, zfile=True)
        fname = zfile.namelist()[0]

        return zfile.open(fname)

    def fetch_data(self):
        """fetch data from OSHA site"""
        for data in self.gen_data_dicts(self.download_file()):
            yield data

    def gen_data_dicts(self, dfile):
        """generate data dictionaries

        args:
            dfile: data csv file

        yields:
            data (dict): data dictionary

        """
        lines = (line.split(',') for line in dfile)

        # get csv headers
        headers = next(lines)

        for line in lines:
            data = dict(zip(headers, line))
            data['hash'] = self.get_hash(data)

            yield data

    def get_insp_url(self):
        """. """
        self.session.get(BASE_URL)

        payload = {'agency': 'osha'}

        soup = self.post_soup(BASE_URL, data=payload)
        url = [a.get('href') for a in
               soup.find('table', {'class': 'download-table'}).find_all('a')
               if 'osha_inspection' in a.get('href')][0]

        url = url.replace('../', '')

        return url

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            data = FedOshaInspection(**data)
            self.save_model(data)

            yield


# ============================================================================
# EOF
# ============================================================================
