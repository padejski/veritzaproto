"""
Module    : integration
Date      : Oct, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza serbia data integration module

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import IntegrityError, transaction

from apps.serbia import models

from apps.corex.utils import are_similar, get_hash


# ============================================================================
# integrator class
# ============================================================================
class SerbiaIntegrator(object):
    """Serbia data integrator class

    """
    def __init__(self):
        """Initialize class """
        self.models = models

    def integrate_officials_companies(self):
        """integrate public officials and companies

        """
        officials = self.models.Official.objects.all()
        companies = self.models.Company.objects.all()

        for off in officials:
            for cmpy in companies:
                for individual in cmpy.individuals:
                    if are_similar(off.name, individual):
                        dat = {'official': off, 'company': cmpy}
                        self.make_save_model(self.models.OfficialCompany, dat)

                        break

    def integrate_officialscompanies_procurement(self):
        """integrate public officials companies in procurement

        """
        officialcompanies = self.models.OfficialCompany.objects.all()
        procurements = self.models.Procurement.objects.all()

        for offcmp in officialcompanies:
            for proc in procurements:
                if are_similar(offcmp.company.company_id, proc.supplier_id):
                    dat = {'official': offcmp.official,
                           'company': offcmp.company,
                           'procurement': proc}
                    self.make_save_model(self.models.OfficialCompanyProcurement, dat)

    def integrate_funders_companies(self):
        """integrate political funders with companies

        """
        companies = self.models.Company.objects.all()
        donations = self.models.ElectionDonation.objects.all()

        for cmpy in companies:
            for donation in donations:
                for individual in cmpy.individuals:
                    if are_similar(individual, donation.donor_name):
                        dat = {'company': cmpy, 'donation': donation}
                        self.make_save_model(self.models.FunderCompany, dat)

                        break

    def integrate_funderscompanies_procurement(self):
        """ integrate political funders companies with procurement

        """
        funderscompanies = self.models.FunderCompany.objects.all()
        procurements = self.models.Procurement.objects.all()

        for cmpy in funderscompanies:
            for proc in procurements:
                if are_similar(cmpy.company.company_id, proc.supplier_id):
                    dat = {'company': cmpy, 'procurement': proc}
                    self.make_save_model(self.models.FunderCompanyProcurement, dat)

    def integrate_fundingcompanies_procurement(self):
        """integrate comapnies that are political funders with procurement

        """
        companies = self.models.FundingCompany.objects.all()
        procurements = self.models.Procurement.objects.all()

        for cmpy in companies:
            for proc in procurements:
                if are_similar(cmpy.company.company_id, proc.supplier_id):
                    dat = {'company': cmpy, 'procurement': proc}
                    self.make_save_model(self.models.FundingCompanyProcurement, dat)

    def make_save_model(self, model, attr_dict):
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
            with transaction.atomic():
                model.save()
            return True
        except IntegrityError:
            return False

    def run(self):
        """run integrations

        """
        self.integrate_funders_companies()
        self.integrate_funderscompanies_procurement()
        self.integrate_fundingcompanies_procurement()
        self.integrate_officials_companies()
        self.integrate_officialscompanies_procurement()


# ============================================================================
# EOF
# ============================================================================
