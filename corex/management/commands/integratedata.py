"""
make data integrations

"""
# ============================================================================
# imports
# ============================================================================
from django.core.management.base import BaseCommand
from django.db import IntegrityError

import serbia.models
from corex.utils import are_similar, get_hash


# ============================================================================
# helpers
# ============================================================================
def integrate_officials_companies():
    """integrate public officials and companies

    """
    officials = serbia.models.Official.objects.all()
    companies = serbia.models.Company.objects.all()

    for off in officials:
        for cmpy in companies:
            for individual in cmpy.individuals:
                if are_similar(off.name, individual):
                    dat = {'official': off, 'company': cmpy}
                    make_save_model(serbia.models.OfficialCompany, dat)

                    break


def integrate_officialscompanies_procurement():
    """integrate public officials companies in procurement

    """
    officialcompanies = serbia.models.OfficialCompany.objects.all()
    procurements = serbia.models.Procurement.objects.all()

    for offcmp in officialcompanies:
        for proc in procurements:
            if are_similar(offcmp.company.company_id, proc.supplier_id.strip()):
                dat = {'official': offcmp.official,
                       'company': offcmp.company,
                       'procurement': proc}
                make_save_model(serbia.models.OfficialCompanyProcurement, dat)


def integrate_politicalfunders_companies():
    """integrate political funders with companies

    """
    companies = serbia.models.Company.objects.all()
    donations = serbia.models.ElectionDonation.objects.all()

    for cmpy in companies:
        for donation in donations:
            for individual in cmpy.individuals:
                if are_similar(individual, donation.donor_name):
                    dat = {'company': cmpy, 'donation': donation}
                    make_save_model(serbia.models.PoliticalFunderCompany, dat)

                    break


def make_save_model(model, attr_dict):
    """make database model instance using attributes dictionary and save it to
    the database.

    make_save_model(model_class, atrributes_dict) -> True / False

    returns:
        True / False (boolean): value depends on if database transaction is
                                successful.
    """
    attr_dict['hash'] = get_hash(attr_dict)
    model = model(**attr_dict)

    try:
        model.save()
        return True
    except IntegrityError:
        return False


# ============================================================================
# data integration: django command
# ============================================================================
class Command(BaseCommand):
    """integration command

    """
    help = "perform data integrations"

    def handle(self, *args, **options):
        """."""
        print('perfoming data integrations')
        # ====================================================================
        # public officials and companies integrations
        # ====================================================================
        integrate_officials_companies()

        # ====================================================================
        # public officials companies in procurement integrations
        # ====================================================================
        integrate_officialscompanies_procurement()

        # ====================================================================
        # political funders companies
        # ====================================================================
        integrate_politicalfunders_companies()
# ============================================================================
# EOF
# ============================================================================
