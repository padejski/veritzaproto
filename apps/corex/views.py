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

from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.core.management import call_command

from apps.core.views import LoginRequiredMixin
from apps.corex import models


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
                               x in models.ScrapeTracker.objects.all()]

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
            thr = threading.Thread(target=call_command, args=('scrape',), kwargs={'scraper': scraper})
            thr.setDaemon(True)
            thr.start()

        elif action == 'stop':
            tracker = models.ScrapeTracker.objects.filter(name=scraper).first()
            tracker.status = 'finished'
            tracker.save()

        else:
            return redirect(request.META.get('HTTP_REFERER'))

        return redirect(request.META.get('HTTP_REFERER'))
