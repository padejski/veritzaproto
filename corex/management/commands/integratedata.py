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
        officials = serbia.models.Official.objects.all()
        companies = serbia.models.Company.objects.all()

        for offcl in officials:
            for cmpy in companies:
                if cmpy.founders:
                    if are_similar(offcl.name, cmpy.founders):
                        dat = {'official': offcl, 'company': cmpy}
                        dat['hash'] = get_hash(dat)
                        model = serbia.models.OfficialCompany(**dat)

                        try:
                            model.save()
                        except IntegrityError:
                            pass

    # ========================================================================
    # public officials companies in procurement integrations
    # ========================================================================
    officialcompanies = serbia.models.OfficialCompany.objects.all()
    procurements = serbia.models.Procurement.objects.all()

    for offcmp in officialcompanies:
        for proc in procurements:
            if are_similar(offcmp.company.company_id, proc.supplier_id.strip()):
                dat = {'official': offcmp.official,
                       'company': offcmp.company,
                       'procurement': proc}
                dat['hash'] = get_hash(dat)
                model = serbia.models.OfficialCompanyProcurement(**dat)

                try:
                    model.save()
                except IntegrityError:
                    pass


# ============================================================================
# EOF
# ============================================================================
