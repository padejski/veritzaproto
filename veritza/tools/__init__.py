from csv import reader as csv_reader
from veritza.apps.core.models import *


class DataReader(object):
    def __init__(self, fname, *args, **kwargs):
        self.file = open(fname)
        self.reader = csv_reader(self.file)
        self.columns = self.reader.next()

    def __iter__(self):
        return self

    def next(self, as_tuple=False):
        if self.reader:
            try:
                if as_tuple:
                    return zip(self.columns, self.reader.next())
                return dict(zip(self.columns, self.reader.next()))
            except ValueError as exc:
                print(exc)

    def close(self):
        self.columns = []
        self.reader = None
        self.file.close()


def insert_companies(fname):
    data = DataReader(fname)
    companies = []
    for record in data:
        c = Company()
        companies.append(c.from_dict(record, commit=False))
        if len(companies) == 100:
            Company.objects.bulk_create(companies)
            companies = []

    # save everything that's left
    if reports:
        Company.objects.bulk_create(companies)


def match_procurements_to_bidders(fname):
    data = DataReader(fname)
    procurements = []

    for idx, record in enumerate(data):
        p = PublicProcurement()
        procurements.append(p.from_dict(record, commit=False))

        b, created = BidderCompany.objects.get_or_create(bidder_id=record.get('bidder_id'))
        if created:
            b.from_dict(record, commit=True)

        c, created = ContractingAuthority.objects.get_or_create(name=record.get('contracting_authority'))
        if created:
            c.from_dict(record, commit=True)

        p.bidder = b
        p.contracting_authority = c

        if len(procurements) == 100:
            PublicProcurement.objects.bulk_create(procurements)
            procurements = []


def insert_procurements(fname):
    data = DataReader(fname)
    procurements = []
    for record in data:
        p = PublicProcurement()
        procurements.append(p.from_dict(record, commit=False))
        if len(procurements) == 100:
            PublicProcurement.objects.bulk_create(procurements)
            procurements = []

    # save everything that's left
    if reports:
        PublicProcurement.objects.bulk_create(procurements)


def insert_bidders(fname):
    data = DataReader(fname)
    bidders = []
    bidder_ids = []
    for record in data:
        if record['bidder_id'].strip() not in bidder_ids:
            b = BidderCompany()
            bidders.append(b.from_dict(record, commit=False))
            bidder_ids.append(b.bidder_id)
        if len(bidders) == 100:
            BidderCompany.objects.bulk_create(bidders)
            bidders = []

    # save everything that's left
    if reports:
        BidderCompany.objects.bulk_create(bidders)


def insert_contracting_authority(fname):
    data = DataReader(fname)
    authorities = []
    authority_ids = []
    for record in data:
        if record['contracting_authority'].strip() not in authority_ids:
            ca = ContractingAuthority()
            authorities.append(ca.from_dict(record, commit=False))
            authority_ids.append(ca.name)
        if len(authorities) == 100:
            ContractingAuthority.objects.bulk_create(authorities)
            authorities = []

    # save everything that's left
    if reports:
        ContractingAuthority.objects.bulk_create(authorities)


def insert_officials_reports(fname):
    data = DataReader(fname)
    reports = []
    reports_ids = []
    for record in data:
        # if record['id'].strip() not in reports_ids:
        por = PublicOfficialReport()
        reports.append(por.from_dict(record, commit=False))
        # reports_ids.append(por.system_id)
        if len(reports) == 100:
            PublicOfficialReport.objects.bulk_create(reports)
            reports = []

    # save everything that's left
    if reports:
        PublicOfficialReport.objects.bulk_create(reports)

# insert_companies('company.csv')
# insert_procurements('procurements.csv')
# insert_bidders('procurements.csv')
# insert_contracting_authority('procurements.csv')
# insert_officials_reports('officials.csv')


companies = []
for c in Company.objects.all():
    if len(companies) == 1000:
        Company.objects