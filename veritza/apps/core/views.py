from django.db.models import Q
from django.db import IntegrityError
from django.views.generic import View, TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest

from django_tables2 import SingleTableView
from report_tools.views import ReportView

from veritza.apps.core.reports import *
from veritza.apps.core.models import *
from veritza.apps.core.tables import *


from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(TemplateView):
    template_name = 'home.html'


class DatasetsView(TemplateView):
    template_name = 'datasets.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class DatasetsView(LoginRequiredMixin, TemplateView):
    template_name = 'datasets.html'


class SubscriptionView(View):

    def post(self, request, **kwargs):
        user = request.user
        dataset = request.POST.get('dataset', '')
        action = request.POST.get('action', '')
        message = ''

        if action == 'subscribe':
            try:
                user.subscribe(dataset)
                message = 'Successfully subscribed for {0}'.format(dataset)
            except IntegrityError as e:
                return redirect(request.path)

        elif action == 'unsubscribe':
            user.unsubscribe(dataset)
            message = 'Successfully unsubscribed from {0}'.format(dataset)

        else:
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))


class ScrapersView(LoginRequiredMixin, TemplateView):
    template_name  = 'scrapers.html'

    def get_context_data(self, **kwargs):
        context = super(ScrapersView, self).get_context_data(**kwargs)
        # context['scrapers'] = Scraper.objects.all()
        context['scrapers'] = [
            {
                'name': 'Companies',
                'status': 'running',
                'last_run': '2015/14/04 16:32'
            },
            {
                'name': 'Procurements',
                'status': 'finished',
                'last_run': '2015/14/04 15:17'
            },
            {
                'name': 'Public officials',
                'status': 'finished',
                'last_run': '2015/14/04 12:02'
            },
        ]
        return context


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'search_results.html'
    searched_classes = [
        PublicOfficial, Company, CompanyMember, PublicProcurement, ElectionsContributions,
        FamilyMember,
    ]

    # TODO: search term need to be at least 3 chars long
    def get(self, request, *args, **kwargs):
        """
        Search all char and text fields of all the models in self.searched_classes.
        Return the search results in the follwing form:
        [
            {
                'model': ' model itself ',
                'model_meta': ' model options ',
                'model_name': ' model name ',
                'objects': 'filtered query set by the search term'
            },
            {...},
            {...}
        ]
        """
        search = request.GET.get('search')
        context = self.get_context_data(**kwargs)
        context['search'] = search
        context['results_count'] = 0

        # Don't search at all if search term is not at least 3 chars long
        if len(search) >= 3:
            datasets = []

            # Prepare filters for every searched class and execute the queries
            # by searching in all char/text fields
            for model in self.searched_classes:
                filters = [
                    Q(**{field.name + '__icontains': search})
                    for field in model._meta.fields if isinstance(field, (models.CharField, models.TextField))
                ]
                query = filters.pop()
                for item in filters:
                    query |= item

                # Execute SQL query to get the results for this model
                objects = model.objects.select_related().filter(query)

                # Add info for this class in the data returned
                datasets.append({
                    'model': model,
                    'model_meta': model._meta,
                    'model_name': model.__name__,
                    'objects': objects
                })
                context['results_count'] += len(objects)

            context['datasets'] = datasets

        return self.render_to_response(context)


class DatasetView(SingleTableView):
    template_name = 'core/list.html'
    stats_template = 'core/stats/empty.html'
    report = None
    filter_class = None

    def get_queryset(self):
        queryset = super(DatasetView, self).get_queryset()
        queryset = queryset.select_related().all()

        search = self.request.GET.get('search')
        if search:
            filters = [
                Q(**{field.name + '__icontains': search})
                for field in queryset.model._meta.fields if isinstance(field, (models.CharField, models.TextField))
            ]
            query = filters.pop()
            for item in filters:
                query |= item

            queryset = queryset.filter(query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(DatasetView, self).get_context_data(**kwargs)
        context['stats_template'] = self.stats_template
        context['search'] = self.request.GET.get('search', '')
        if self.report:
            context['report'] = self.report
        return context


class PublicOfficialsView(LoginRequiredMixin, DatasetView, ReportView):
    model = PublicOfficial
    table_class = PublicOfficialTable
    stats_template = 'core/stats/public_officials.html'
    report = PublicOfficialsReport()

    def get_queryset(self):
        queryset = super(PublicOfficialsView, self).get_queryset()
        return queryset.prefetch_related('publicofficialreport_set').all()


class PublicOfficialDetailsView(LoginRequiredMixin, DetailView):
    model = PublicOfficial
    template_name = 'core/details/public_official.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        obj.reports = PublicOfficialReport.objects.filter(official_id=obj.id)
        obj.official_companies = PublicOfficialCompany.objects.select_related('company').filter(official_id=obj.id)
        return obj


class CompaniesView(LoginRequiredMixin, DatasetView):
    model = Company
    table_class = CompanyTable
    stats_template = 'core/stats/companies.html'
    report = CompaniesReport()

    def get_queryset(self):
        queryset = super(self.__class__, self).get_queryset()
        return queryset.prefetch_related('companymember_set', 'biddercompany_set').all()


class CompanyDetailsView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'core/details/company.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        obj.company_members = CompanyMemberTitle.objects.select_related('company_member').filter(company_registration_number=obj.registration_number)
        obj.company_procurements = [bidder_company.procurement for bidder_company in BidderCompany.objects.select_related().filter(company_id=obj.id)]
        return obj


class CompanyMembersView(LoginRequiredMixin, DatasetView):
    model = CompanyMember
    table_class = CompanyMemberTable

    def get_queryset(self):
        queryset = super(self.__class__, self).get_queryset()
        # 'company' field needs to be explicitly requested here as
        # it is null=True and not select_related by default
        return queryset.select_related('company').all()


class CompanyMemberDetailsView(LoginRequiredMixin, DetailView):
    model = CompanyMember
    template_name = 'core/details/company_member.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        obj.titles = CompanyMemberTitle.objects.filter(company_member_id=obj.id)
        return obj


class FamilyMembersView(LoginRequiredMixin, DatasetView, ReportView):
    model = FamilyMember
    table_class = FamilyMemberTable
    stats_template = 'core/stats/family_members.html'
    report = FamilyMembersReport()


class FamilyMemberDetailsView(LoginRequiredMixin, DetailView):
    model = FamilyMember
    template_name = 'core/details/family_member.html'

    def get_queryset(self):
        queryset = super(FamilyMemberDetailsView, self).get_queryset()
        return queryset.select_related()


class PublicProcurementsView(LoginRequiredMixin, DatasetView, ReportView):
    model = PublicProcurement
    table_class = PublicProcurementTable
    stats_template = 'core/stats/procurements.html'
    report = ProcurementsReport()


class PublicProcurementDetailsView(LoginRequiredMixin, DetailView):
    model = PublicProcurement
    template_name = 'core/details/public_procurement.html'

    def get_object(self, **kwargs):
        obj = super(PublicProcurementDetailsView, self).get_object(**kwargs)
        obj.winners = BidderCompany.objects.select_related('company').filter(procurement_id=obj.id)
        return obj


class BidderCompaniesView(LoginRequiredMixin, DatasetView):
    model = BidderCompany
    table_class = BidderCompanyTable


class BidderCompanyDetailsView(LoginRequiredMixin, DatasetView):
    model = BidderCompany


class ElectionsContributionsView(LoginRequiredMixin, DatasetView, ReportView):
    model = ElectionsContributions
    table_class = ElectionsContributionsTable
    stats_template = 'core/stats/elections_contributions.html'
    report = ElectionsContributionsReport()


class ElectionsContributionsDetailsView(DetailView):
    model = ElectionsContributions
    template_name = 'core/details/elections_contributions.html'

    def get_object(self, **kwargs):
        obj = super(self.__class__, self).get_object(**kwargs)
        return obj


class PublicOfficialCompaniesView(LoginRequiredMixin, DatasetView):
    model = PublicOfficialCompany
    table_class = PublicOfficialCompanyTable


class PublicOfficialCompanyDetailsView(LoginRequiredMixin, DetailView):
    model = PublicOfficialCompany


class ConflictInterestsView(LoginRequiredMixin, DatasetView):
    model = ConflictInterest
    table_class = ConflictInterestTable


class ConflictInterestDetailsView(LoginRequiredMixin, DetailView):
    model = ConflictInterest


class FamilyMemberCompaniesView(LoginRequiredMixin, DatasetView):
    model = FamilyMemberCompany
    table_class = FamilyMemberCompanyTable


class FamilyMemberCompanyDetailsView(LoginRequiredMixin, DatasetView):
    model = FamilyMemberCompany


class ConflictInterestFamilyMembersView(LoginRequiredMixin, DatasetView):
    model = ConflictInterestFamilyMember
    table_class = ConflictInterestFamilyMemberTable


class ConflictInterestFamilyMemberDetailsView(LoginRequiredMixin, DatasetView):
    model = ConflictInterestFamilyMember
