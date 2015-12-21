# -*- coding: utf-8 -*-
"""
Toxics Release Inventory Scraper

http://www.epa.gov/enviro/html/frs_demo/geospatial_data/geo_data_state_single.html

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
import re

from corex.basescraper import BaseScraper
from ..models import FedToxicsFacility

# ============================================================================
# useful constants
# ============================================================================
BASE_URL = 'http://www.epa.gov/enviro/html/frs_demo/geospatial_data/geo_data_state_single.html'
DATA_HEADERS = ['accuracy_value', 'census_block_code', 'city_name',
                'collect_desc', 'congressional_dist_num', 'conveyor',
                'country_name', 'county_name', 'create_date', 'epa_region_code',
                'federal_agency_name', 'federal_facility_code', 'fips_code',
                'frs_facility_detail_report_url', 'hdatum_desc', 'huc_code',
                'interest_types', 'latitude83', 'location_address',
                'location_description', 'longitude83', 'naics_code_descriptions',
                'naics_codes', 'pgm_sys_acrnms', 'postal_code', 'primary_name',
                'ref_point_desc', 'registry_id', 'sic_code_descriptions',
                'sic_codes', 'site_type_name', 'source_desc', 'state_code',
                'state_name', 'supplemental_location', 'tribal_land_code',
                'tribal_land_name', 'update_date', 'us_mexico_border_ind']


# ============================================================================
# scraper implementation
# ============================================================================
class ToxicsInventoryScraper(BaseScraper):
    """Toxics Inventory Scraper"""

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def download_files(self, file_urls):
        """download zip files"""
        for url in file_urls:
            zip_file = self.download_http(url, zfile=True)

            yield zip_file

    def fetch_data(self):
        """fetch data from epa website"""
        for zfile in self.download_files(self.gen_file_urls()):
            for data in self.gen_data_dicts(zfile):
                yield data

    def gen_data_dicts(self, zfile):
        """generate data dictionaries
        """
        lines = (line for line in self.get_file_from_zip('state_single', zfile))
        next(lines)  # discard csv headers

        for line in lines:
            data = dict(zip(DATA_HEADERS, line.split(',')))
            # clean data values
            for key, val in data.iteritems():
                data[key] = re.sub(r'^"|"$', '', val)

            data['hash'] = self.get_hash(data)

            yield data

    def gen_file_urls(self):
        """generate zip files urls"""
        form = self.get_soup(BASE_URL).find('form', {'method': 'post'})
        urls = (opt.get('value') for opt in form.find_all('option'))

        for url in urls:
            yield url

    @staticmethod
    def get_file_from_zip(fname, zfile):
        """get file from zip"""
        for name in zfile.namelist():
            if fname in name.lower():
                return zfile.open(name)

    def run(self):
        """run scraper """
        for data in self.fetch_data():
            data = FedToxicsFacility(**data)
            self.save_model(data)

            yield

# ============================================================================
# EOF
# ============================================================================
