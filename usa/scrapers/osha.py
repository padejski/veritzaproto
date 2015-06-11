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
from ..models import FedOshaEbsa

# ============================================================================
# useful constants
# ============================================================================
EBSA_URL = 'http://prd-enforce-xfr-02.dol.gov/data_catalog/EBSA/ebsa_ocats_20150402.csv.zip'
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
        zfile = self.download_http(EBSA_URL, zfile=True)

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

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            data = FedOshaEbsa(**data)
            self.save_model(data)

# ============================================================================
# EOF
# ============================================================================
