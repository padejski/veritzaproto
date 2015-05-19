"""
USA Procurements Scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = April 2015

"""
from itertools import imap

from xmltodict import parse as xmlparse
from django.db.utils import IntegrityError

from corex.basescraper import BaseScraper
from .models import FedCompany as Company
from .models import FedProcurement as Procurement
from . import constants as const


class FedContractsScraper(BaseScraper):
    """USA Federal Procurements Contracts Scraper"""

    def __init__(self):
        """Initialize scraper"""
        BaseScraper.__init__(self)

    def fetch_data(self):
        """Fetch and parse api data

        """
        docs = imap(self.filter_doc, self.parse_xml())
        model_dicts = imap(self.make_model_dicts, docs)

        for (contract, vendor) in model_dicts:
            yield (contract, vendor)

    @staticmethod
    def get_max_record(data_dict):
        """Get number of records found

        """
        return int(data_dict['usaspendingSearchResults']['result']['@numFound'])

    def get_xml(self, url):
        """Fetch XML data from api url endpoint

        """
        xml = self.get(url).content

        return xml

    def parse_xml(self):
        """Parse xml data to dictionary records

        """
        max_records = self.get_max_record(
            xmlparse(self.get_xml(const.CONTRACTS_URL)))

        for start in range(0, max_records, 1000):
            url = const.CONTRACTS_URL + '&records_from={}'.format(start)
            dic = xmlparse(self.get_xml(url))
            docs = dic['usaspendingSearchResults']['result']['doc']

            for doc in docs:
                yield doc

    @staticmethod
    def filter_dict(dic, filter_keys):
        """Filter dictionary to remain with filter keys

        """
        new_dict = {key: dic.get(key) for key in filter_keys}

        return new_dict

    @staticmethod
    def filter_doc(doc):
        """Filter out unneeded keys from doc dictionary

        """
        new_doc = {key: doc.get(key) for key in const.DOC_KEYS}
        new_doc['url'] = const.CONTRACTS_URL

        return new_doc

    def make_model_dicts(self, doc):
        """make model dictionaries from doc dictionary

        """
        data = {const.KEYS_MAP.get(key): value for key, value in doc.items()}

        contract = self.filter_dict(data, const.CONTRACT_KEYS)
        contract['date'] = self.str2date(contract['date'], "%Y-%m-%d", sep='T')

        vendor = self.filter_dict(data, const.COMPANY_KEYS)
        vendor['type'] = data['company_type']
        vendor['reg_date'] = self.str2date(vendor['reg_date'], "%Y-%m-%d", sep='T')

        return (contract, vendor)

    def run(self):
        """Run scraper

        """
        for contract, vendor in self.fetch_data():
            self.save_models(contract, vendor)
            yield

    def save_models(self, contract, vendor):
        """Make and save models to database

        """
        vendor['hash'] = self.get_hash(vendor)
        vmodel = Company(**vendor)

        try:
            vmodel.save()
        except IntegrityError as err:
            print(err)
            return False
        else:
            contract['vendor_id'] = vmodel.id
            contract['hash'] = self.get_hash(contract)
            cmodel = Procurement(**contract)

        try:
            cmodel.save()
        except IntegrityError:
            pass


if __name__ == '__main__':
    FedContractsScraper().run()
# ============================================================================
# EOF
# ============================================================================
