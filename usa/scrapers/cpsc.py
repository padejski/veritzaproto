# -*- coding: utf-8 -*-
"""
Consumer Product Safety Commission Scraper

http://www.cpsc.gov/en/Recalls/CPSC-Recalls-Application-Program-Interface-API-Information/

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
from corex.basescraper import BaseScraper
from ..models import FedCpscRecall

# ============================================================================
# useful constants
# ============================================================================
REC_URL = 'http://www.saferproducts.gov/RestWebServices/Recall?format=json'


# ============================================================================
# scrapers implementation
# ============================================================================
class CpscRecallsScraper(BaseScraper):
    """Federal Consumer Product Safety Commission Recalls Scraper"""

    def __init__(self):
        """Initialize base class"""
        BaseScraper.__init__(self)

    def fetch_data(self):
        """fetch data from json api"""
        for data in self.parse_raw_dicts(self.gen_raw_dicts()):
            yield data

    def gen_raw_dicts(self):
        """generate raw json data"""

        for raw_dict in self.session.get(REC_URL).json():
            yield raw_dict

    @staticmethod
    def get_key_val(dicts, key='Name'):
        """get key value from a list of dicts"""
        return ','.join((d.get(key) for d in dicts))

    def parse_raw_dict(self, rdict):
        """parse raw json data """
        data = {}

        data['recall_id'] = rdict['RecallID']
        data['recall_date'] = rdict['RecallDate']
        data['recall_num'] = rdict['RecallNumber']
        data['desc'] = rdict['Description']
        data['title'] = rdict['Title']
        data['url'] = rdict['URL']
        data['last_pub_date'] = rdict['LastPublishDate']
        data['mfcs'] = rdict['Manufacturers']
        data['hazards'] = self.get_key_val(rdict['Hazards'])
        data['consumer_contact'] = rdict['ConsumerContact']
        data['images'] = self.get_key_val(rdict['Images'], key='URL')
        data['product_upcs'] = rdict['ProductUPCs']
        data['products'] = self.get_key_val(rdict['Products'])
        data['retailers'] = self.get_key_val(rdict['Retailers'])
        data['in_conj'] = self.get_key_val(rdict['Inconjunctions'], key='Country')
        data['remedies'] = self.get_key_val(rdict['Remedies'])
        data['injuries'] = self.get_key_val(rdict['Injuries'])
        data['mfcs_countries'] = self.get_key_val(rdict['ManufacturerCountries'], key='Country')

        data['hash'] = self.get_hash(data)

        return data

    def parse_raw_dicts(self, dicts):
        """parse raw json data"""
        for dic in dicts:
            yield self.parse_raw_dict(dic)

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            print(data)
            data = FedCpscRecall(**data)
            self.save_model(data)

            yield

# ============================================================================
# EOF
# ============================================================================
