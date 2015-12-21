# -*- coding: utf-8 -*-
"""
Elections Canditates and Donors Info Scraper

http://www.fec.gov/finance/disclosure/ftpdet.shtml

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
from itertools import imap

from apps.corex.basescraper import BaseScraper
from ..models import FedCandidate, FedElectionContribution

# ============================================================================
# useful constants
# ============================================================================
CAND_HEADERS = ['cand_id', 'cand_name', 'cand_pty_affiliation',
                'cand_election_yr', 'cand_office_st', 'cand_office',
                'cand_office_district', 'cand_ici', 'cand_status',
                'cand_pcc', 'cand_st1', 'cand_st2', 'cand_city',
                'cand_st', 'cand_zip']

CAND_MASTER_FILES_URLS = ['ftp://ftp.fec.gov/FEC/2016/cn16.zip',
                          'ftp://ftp.fec.gov/FEC/2014/cn14.zip',
                          'ftp://ftp.fec.gov/FEC/2012/cn12.zip']

COMM_HEADERS = ['cmte_id', 'amndt_ind', 'rpt_tp', 'transaction_pgi',
                'image_num', 'transaction_tp', 'entity_tp', 'name',
                'city', 'state', 'zip_code', 'employer', 'occupation',
                'transaction_dt', 'transaction_amt', 'other_id',
                'cand_id', 'tran_id', 'file_num', 'memo_cd',
                'memo_text', 'sub_id']

COMM_FILES_URLS = ['ftp://ftp.fec.gov/FEC/2016/pas216.zip',
                   'ftp://ftp.fec.gov/FEC/2014/pas214.zip',
                   'ftp://ftp.fec.gov/FEC/2012/pas212.zip']

INDV_HEADERS = ['cmte_id', 'amndt_ind', 'rpt_tp', 'transaction_pgi',
                'image_num', 'transaction_tp', 'entity_tp', 'name',
                'city', 'state', 'zip_code', 'employer', 'occupation',
                'transaction_dt', 'transaction_amt', 'other_id', 'tran_id',
                'file_num', 'memo_cd', 'memo_text', 'sub_id']

INDV_FILES_URLS = ['ftp://ftp.fec.gov/FEC/2016/indiv16.zip',
                   'ftp://ftp.fec.gov/FEC/2014/indiv14.zip',
                   'ftp://ftp.fec.gov/FEC/2012/indiv12.zip']

AMENDMENT_MAP = {'n': 'new',
                 'a': 'amendment to previous report',
                 't': 'termination report'}

ENTITY_MAP = {'can': 'Candidate',
              'ccm': 'Candidate Committee',
              'com': 'Committee',
              'ind': 'Individual',
              'org': 'Organization',
              'pac': 'Political Action Committee',
              'pty': 'Party Organization'}

ICI_MAP = {'c': 'Challenger',
           'i': 'Incumbent',
           'o': 'Open Seat'}

OFFICE_MAP = {'h': 'House',
              'p': 'President',
              's': 'senate'}

PARTY_MAP = {'rep': 'Republican',
             'ind': 'Independent',
             'dem': 'Democratic'}

REPORT_MAP = {'12c': 'pre-convention', '12g': 'pre-general',
              '12p': 'pre-primary', '12r': 'pre-run-off',
              '12s': 'pre-special', '24h': '24 hour notification',
              '30d': 'post-election', '30g': 'post-general',
              '30p': 'post-primary', '30r': 'post-run-off',
              '30s': 'post-special', '48h': '48 hour notification',
              '60d': 'post-convention', '90d': 'post inaugural',
              '90s': 'post inaugural supplement', 'adj': 'comp adjust amend',
              'ca': 'comprehensive amend', 'm10': 'october monthly',
              'm11': 'november monthly', 'm12': 'december monthly',
              'm2': 'february monthly', 'm3': 'march monthly',
              'm4': 'april monthly', 'm5': 'may monthly',
              'm6': 'june monthly', 'm7': 'july monthly',
              'm8': 'august monthly', 'm9': 'september monthly',
              'my': 'mid-year report', 'q1': 'april quarterly',
              'q2': 'july quarterly', 'q3': 'october quarterly',
              'ter': 'termination report', 'ye': 'year-end'}

STATUS_MAP = {'c': 'Statutory candidate',
              'f': 'Statutory candidate for future election',
              'n': 'Not yet a statutory candidate',
              'p': 'Statutory candidate in prior cycle'}


# ============================================================================
# scraper implementation
# ============================================================================
class CommitteeContributionsScraper(BaseScraper):
    """Committee Contributions Scraper"""

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def download_cfiles(self):
        """fetch contribution files"""
        for url in COMM_FILES_URLS:
            cfile = self.download_ftp(url, zfile=True)

            yield cfile.open('itpas2.txt')

    def fetch_data(self):
        """fetch  contributions data"""
        for data in self.gen_data_dicts(self.download_cfiles()):
            yield data

    def gen_data_dicts(self, cfiles):
        """generate contribution data dictionaries from data files"""
        for gen in imap(self.gen_data_dict, cfiles):
            for data in gen:
                yield data

    def gen_data_dict(self, cfile):
        """generate data dicts from file"""
        for line in cfile:
            data = dict(zip(COMM_HEADERS, line.lower().split('|')))
            data = self.map_abbrvs(data)
            data['hash'] = self.get_hash(data)

            yield data

    @staticmethod
    def map_abbrvs(data):
        """map abbreviations to full words"""
        data['entity_tp'] = ENTITY_MAP[data['entity_tp']]
        data['rpt_tp'] = REPORT_MAP[data['rpt_tp']]

        return data

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            data = FedElectionContribution(**data)
            self.save_model(data)

            yield


class ElectionCandsScraper(BaseScraper):
    """Election Contributions scraper"""

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def download_mfiles(self):
        """fetch candidate master files"""
        for url in CAND_MASTER_FILES_URLS:
            mfile = self.download_ftp(url, zfile=True)

            yield mfile.open('cn.txt')

    def fetch_data(self):
        """fetch canditates date"""
        for data in self.gen_cand_dicts(self.download_mfiles()):
            yield data

    def gen_cand_dict(self, cfile):
        """generate candidates info dict from data file

        args:
            cfile (fileobj): canditates master file

        yields:
            cand (dict): candidate info dictionary
        """
        for line in cfile:
            cand = dict(zip(CAND_HEADERS, line.lower().split('|')))
            cand = self.map_abbrvs(cand)
            cand['hash'] = self.get_hash(cand)

            yield cand

    def gen_cand_dicts(self, cfiles):
        """generate canddate info dicts from master files"""
        for gen in imap(self.gen_cand_dict, cfiles):
            for cand in gen:
                yield cand

    @staticmethod
    def map_abbrvs(data):
        """map abbreviations to full words"""
        data['cand_pty_affiliation'] = PARTY_MAP.get(data['cand_pty_affiliation'], data['cand_pty_affiliation'])
        data['cand_ici'] = ICI_MAP.get(data['cand_ici'], data['cand_ici'])
        data['cand_office'] = OFFICE_MAP.get(data['cand_office'], data['cand_office'])
        data['cand_status'] = STATUS_MAP.get(data['cand_status'], data['cand_status'])

        return data

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            cand = FedCandidate(**data)
            self.save_model(cand)

            yield


class IndividualContributionsScraper(BaseScraper):
    """Individual Contributions Scraper"""

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def download_files(self):
        """fetch individual contribution files"""
        for url in INDV_FILES_URLS:
            ifile = self.download_ftp(url, zfile=True)

            yield ifile.open('itcont.txt')

    def fetch_data(self):
        """fetch individuals contributions data"""
        for data in self.gen_data_dicts(self.download_files()):
            yield data

    def gen_data_dicts(self, ifiles):
        """generate contribution data dictionaries from data files"""
        for gen in imap(self.gen_data_dict, ifiles):
            for data in gen:
                yield data

    def gen_data_dict(self, ifile):
        """generate data dicts from file"""
        for line in ifile:
            data = dict(zip(INDV_HEADERS, line.lower().split('|')))
            data = self.map_abbrvs(data)
            data['hash'] = self.get_hash(data)

            yield data

    @staticmethod
    def map_abbrvs(data):
        """map abbreviations to full words"""
        data['entity_tp'] = ENTITY_MAP[data['entity_tp']]
        data['rpt_tp'] = REPORT_MAP[data['rpt_tp']]

        return data

    def run(self):
        """run scraper"""
        for data in self.fetch_data():
            data = FedElectionContribution(**data)
            self.save_model(data)

            yield
# ============================================================================
# EOF
# ============================================================================
