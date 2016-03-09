"""
Module    : integration
Date      : Oct, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza federal usa data integration module

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import IntegrityError, transaction

from apps.usa import models

from apps.corex.utils import are_similar, get_hash


# ============================================================================
# integrator class
# ============================================================================
class UsaIntegrator(object):
    """USA Federal data integrator class

    """
    def __init__(self):
        """Initialize class """
        self.models = models

    def integrate_funders_companies(self):
        """integrate political funders with companies

        """
        companies = self.models.Company.objects.all()
        donations = self.models.FedElectionContribution.objects.all()

        for cmpy in companies:
            for donation in donations:
                for individual in cmpy.individuals:
                    if are_similar(individual, donation.name):
                        dat = {'company': cmpy, 'donation': donation}
                        self.make_save_model(self.models.FedFunderCompany, dat)

                        break

    def integrate_funderscompanies_procurement(self):
        """ integrate political funders companies with procurement

        """
        funderscompanies = self.models.FedFunderCompany.objects.all()
        procurements = self.models.FedProcurement.objects.all()

        for cmpy in funderscompanies:
            for proc in procurements:
                if are_similar(cmpy.company.id, proc.vendor_id):
                    dat = {'company': cmpy, 'procurement': proc}
                    self.make_save_model(self.models.FedFunderCompanyProcurement, dat)

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


# ============================================================================
# EOF
# ============================================================================
