"""
Module    : views
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza core views


"""
# ============================================================================
# necessary imports
# ============================================================================
import threading

import watson
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.core.management import call_command

from apps.core.views import LoginRequiredMixin
from apps.corex import models
from apps.core import models as Mmodels  # montenegro models
from apps.serbia import models as Smodels  # serbia models


# ============================================================================
# class based views
# ============================================================================
class IndexView(TemplateView):
    template_name = 'home.html'


class DatasetsView(TemplateView):
    template_name = 'core_datasets.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ScrapersView(LoginRequiredMixin, TemplateView):
    template_name = 'scrapers.html'

    def get_context_data(self, **kwargs):
        context = super(ScrapersView, self).get_context_data(**kwargs)
        context['scrapers'] = [{'name': x.name, 'status': x.status, 'last_run': x.last_run} for
                               x in models.ScrapeTracker.objects.order_by('name').all()]

        return context


class SubscriptionView(View):

    def post(self, request, **kwargs):
        user = request.user
        dataset = request.POST.get('dataset', '')
        action = request.POST.get('action', '')
        app = request.POST.get('app', None)
        message = ''

        if action == 'subscribe':
            try:
                user.subscribe(dataset, app)
                message = 'Successfully subscribed for {0}'.format(dataset)
            except IntegrityError:
                return redirect(request.path)

        elif action == 'unsubscribe':
            user.unsubscribe(dataset, app)
            message = 'Successfully unsubscribed from {0}'.format(dataset)

        else:
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))

class ScrapeView(View):

    def post(self, request, **kwargs):
        user = request.user
        scraper = request.POST.get('scraper', '')
        action = request.POST.get('action', '')

        if action == 'run':
            if 'monte' in scraper.lower():
                args = 'run_scraper {}'.format(scraper.split(':')[-1])
                thr = threading.Thread(target=call_command, args=(args,))
            else:
                thr = threading.Thread(target=call_command,
                                       args=('scrape',),
                                       kwargs={'scraper': scraper})

            thr.setDaemon(True)
            thr.start()

        elif action == 'stop':
            tracker = models.ScrapeTracker.objects.filter(name=scraper).first()
            tracker.status = 'finished'
            tracker.save()

        else:
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))


class SearchView(LoginRequiredMixin, TemplateView):
    """global search view"""
    template_name = 'core_search_results.html'

    def get(self, request, *args, **kwargs):
        """search term"""
        search_term = request.GET.get('search')
        context = self.get_context_data(**kwargs)
        context['search'] = search_term
        context['results_count'] = 0
        context['datasets'] = []

        _models = (Smodels.Company, Smodels.ElectionDonation, Smodels.Procurement,
                   Smodels.Official, Mmodels.ContributorCompanyProcurement,
                   Mmodels.ContributorIndividualProcurement, Mmodels.ElectionsContributions,
                   Mmodels.ElectionsContributionCompany, Mmodels.ElectionsContributionCompanyMember,
                   Mmodels.PublicOfficial, Mmodels.PublicOfficialReport, Mmodels.FamilyMember,
                   Mmodels.FamilyMemberCompany, Mmodels.Company, Mmodels.CompanyMember,
                   Mmodels.CompanyMemberTitle, Mmodels.BidderCompany, Mmodels.ProcurementCompanyRaw,
                   Mmodels.ProcurementCompany, Mmodels.ContractingAuthority, Mmodels.PublicProcurement,
                   Mmodels.PublicOfficialCompany, Mmodels.ConflictInterestFamilyMember,
                   Mmodels.ConflictInterest)

        for model in _models:
            results = watson.filter(model, search_term)
            context['results_count'] += len(results)
            context['datasets'].append({
                'model': model,
                'model_meta': model._meta,
                'model_name': model.__name__,
                'objects': results
            })

        return self.render_to_response(context)

# ============================================================================
# EOF
# ============================================================================
