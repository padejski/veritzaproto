# -*- coding: utf-8 -*-
"""
Module    : admin
Date      : September, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza serbia admin

"""
# ============================================================================
# necessary imports
# ============================================================================
from django.contrib import admin
from serbia.models import Company, Procurement, Official, ElectionDonation


# ============================================================================
# ModelAdmin objects
# ============================================================================
class CompanyAdmin(admin.ModelAdmin):
    """Company representation in the admin interface"""
    pass


class ElectionDonationAdmin(admin.ModelAdmin):
    """Election Donation representation in the admin interface"""
    pass


class OfficialAdmin(admin.ModelAdmin):
    """Official representation in the admin interface"""
    pass


class ProcurementAdmin(admin.ModelAdmin):
    """Procurement representation in the admin interface"""
    pass


# ============================================================================
# register ModelAdmin objects
# ============================================================================
admin.site.register(Company, CompanyAdmin)
admin.site.register(ElectionDonation, ElectionDonationAdmin)
admin.site.register(Official, OfficialAdmin)
admin.site.register(Procurement, ProcurementAdmin)

# ============================================================================
# EOF
# ============================================================================
