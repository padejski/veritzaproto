# -*- coding: utf-8 -*-
"""
IRS Exempt Organizations Info Scraper

http://apps.irs.gov/app/eos/forwardToPub78Download.do

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
from corex.basescraper import BaseScraper
from ..models import FedIrsExemptOrg

# ============================================================================
# useful constants
# ============================================================================
FILE_URL = 'http://apps.irs.gov/pub/epostcard/data-download-pub78.zip'
HEADERS = ['ein', 'name', 'city', 'state', 'country', 'status']


# ============================================================================
# scraper implementation
# ============================================================================
class IrsExemptScraper(BaseScraper):
    """IRS Exempt Organizations Scraper"""

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def download_file(self):
        """fetch and deflate zip data file"""
        zfile = self.download_http(FILE_URL, zfile=True)

        return zfile.open('data-download-pub78.txt')

    def fetch_data(self):
        """fetch irs exempt organizations data"""
        for data in self.gen_data_dicts(self.download_file()):
            yield data

    def gen_data_dicts(self, dfile):
        """generate data dicts using rows from data file

        args:
            dfile (fileobj): data file

        yields:
            data (dict): data dictionary

        """
        for line in dfile:
            if '|' in line:
                data = dict(zip(HEADERS, line.lower().split('|')))
                data['hash'] = self.get_hash(data)

                yield data

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            print(data)
            data = FedIrsExemptOrg(**data)
            self.save_model(data)

            yield

# ============================================================================
# EOF
# ============================================================================
