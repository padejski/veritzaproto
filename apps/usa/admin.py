# -*- coding: utf-8 -*-
"""
Module    : admin
Date      : February, 2016
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza usa admin

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.contrib import admin
from apps.usa import models


# ============================================================================
# ModelAdmin objects
# ============================================================================
class FedCandidateAdmin(admin.ModelAdmin):
    """Candidate representation in the admin interface"""
    pass


class FedCompanyAdmin(admin.ModelAdmin):
    """Company representation in the admin interface"""
    pass


class FedElectionContributionAdmin(admin.ModelAdmin):
    """Election Donation representation in the admin interface"""
    pass


class FedIrsExemptOrgAdmin(admin.ModelAdmin):
    """IRS Exempt organization representation in the admin interface"""
    pass


class FedProcurementAdmin(admin.ModelAdmin):
    """Procurement representation in the admin interface"""
    pass


class FedFinancialDisclosureAdmin(admin.ModelAdmin):
    """Financial Disclosure representation in the admin interface"""
    pass


class FedSecFilingAdmin(admin.ModelAdmin):
    """SEC Filing representation in the admin interface"""
    pass


class FedToxicsFacilityAdmin(admin.ModelAdmin):
    """Toxics facility representation in the admin interface"""
    pass


class FedOshaEbsaAdmin(admin.ModelAdmin):
    """Osha Ebsa representation in the admin interface"""
    pass


class FedOshaInspectionAdmin(admin.ModelAdmin):
    """Osha Inspection representation in the admin interface"""
    pass


class FedCpscRecallAdmin(admin.ModelAdmin):
    """Cpsc Recall representation in the admin interface"""
    pass


class FedCpscRecallViolationAdmin(admin.ModelAdmin):
    """Cpsc Recall Violation representation in the admin interface"""
    pass


# ============================================================================
# register ModelAdmin objects
# ============================================================================
admin.site.register(models.FedCandidate, FedCandidateAdmin)
admin.site.register(models.FedCompany, FedCompanyAdmin)
admin.site.register(models.FedElectionContribution, FedElectionContributionAdmin)
admin.site.register(models.FedIrsExemptOrg, FedIrsExemptOrgAdmin)
admin.site.register(models.FedProcurement, FedProcurementAdmin)
admin.site.register(models.FedFinancialDisclosure, FedFinancialDisclosureAdmin)
admin.site.register(models.FedSecFiling, FedSecFilingAdmin)
admin.site.register(models.FedToxicsFacility, FedToxicsFacilityAdmin)
admin.site.register(models.FedOshaEbsa, FedOshaEbsaAdmin)
admin.site.register(models.FedOshaInspection, FedOshaInspectionAdmin)
admin.site.register(models.FedCpscRecall, FedCpscRecallAdmin)
admin.site.register(models.FedCpscRecallViolation, FedCpscRecallViolationAdmin)

# ============================================================================
# EOF
# ============================================================================
