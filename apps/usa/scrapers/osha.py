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
from apps.corex.basescraper import BaseScraper
from ..models import FedOshaEbsa, FedOshaInspection

# ============================================================================
# useful constants
# ============================================================================
BASE_URL = 'http://ogesdw.dol.gov/views/data_summary.php'
EBSA_HEADERS = ['case_type', 'ein', 'pn', 'plan_year', 'plan_name', 'plan_admin',
                'plan_admin_state', 'plan_admin_zip_code', 'final_close_reason',
                'final_close_date', 'penalty_amount']
OSHA_HEADERS = ['activity_nr', 'reporting_id', 'state_flag', 'estab_name',
                'site_address', 'site_city', 'site_state', 'site_zip',
                'owner_type', 'owner_code', 'adv_notice', 'safety_hlth',
                'sic_code', 'naics_code', 'insp_type', 'insp_scope',
                'why_no_insp', 'union_status', 'safety_manuf', 'safety_const',
                'safety_marit', 'health_manuf', 'health_const', 'health_marit',
                'migrant', 'mail_street', 'mail_city', 'mail_state', 'mail_zip',
                'host_est_key', 'nr_in_estab', 'open_date', 'case_mod_date',
                'close_conf_date', 'close_case_date', 'open_year',
                'case_mod_year', 'close_conf_year', 'close_case_year',
                'osha_accident_indicator', 'violation_type_s', 'violation_type_o',
                'violation_type_r', 'violation_type_u', 'violation_type_w',
                'inspection_to_filter']



# ============================================================================
# scrapers implementation
# ============================================================================
class OshaEbsaScraper(BaseScraper):
    """OSHA EBSA Enforcement data scraper"""
    NAME = 'usa:osha'

    def __init__(self):
        """init base class"""
        BaseScraper.__init__(self)

    def download_file(self):
        """download and deflate zip data file"""
        ebsa_url = self.get_ebsa_url()
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

        # get rid of headers
        next(lines)

        for line in lines:
            data = dict(zip(OSHA_HEADERS, line))
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
