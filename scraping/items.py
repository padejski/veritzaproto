# -*- coding: utf-8 -*-

import dateutil
import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from veritza.apps.core.models import (
    PublicOfficial, PublicOfficialReport, Company,
    CompanyMember, PublicProcurement, ProcurementCompanyRaw, ContractingAuthority
)


class PublicOfficialItem(DjangoItem):
    django_model = PublicOfficial

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()


class PublicOfficialReportItem(DjangoItem):
    django_model = PublicOfficialReport

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()


class CompanyItem(DjangoItem):
    django_model = Company

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()

    @classmethod
    def from_dict(cls, data):
        instance = CompanyItem()
        instance["registration_number"] = data.get('registarski_broj', "").strip()
        instance["identification_number"] = data.get('maticni_broj', "").strip()
        instance["name"] = data.get(u'naziv_društva', "").strip()
        instance["full_name"] = data.get('full_name', "").strip()
        instance["address"] = data.get('address', "").strip()
        instance["mail_address"] = data.get('mail_address', "").strip()
        instance["status"] = data.get('status', "").strip()
        instance["registration_date"] = dateutil.parser.parse(data.get('registration_date', ""))
        instance["location"] = data.get('mjesto', "").strip()
        instance["activity"] = data.get('djelatnost', "").strip()
        instance["economic_activity"] = data.get('naziv_privredne_djelatnosti', "").strip()
        instance["link"] = data.get('link', "").strip()
        return instance


class CompanyMemberItem(DjangoItem):
    django_model = CompanyMember

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()


class PublicProcurementItem(DjangoItem):
    django_model = PublicProcurement

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()


class ProcurementCompanyItem(DjangoItem):
    django_model = ProcurementCompanyRaw

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()


class ContractingAuthorityItem(DjangoItem):
    django_model = ContractingAuthority

    uuid = scrapy.Field()
    created_by = scrapy.Field()
    # modified_by = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    active = scrapy.Field()
