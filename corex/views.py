"""
Module    : views
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza core views


"""
# ============================================================================
# necessary imports
# ============================================================================
from django.db import IntegrityError
from django.shortcuts import redirect
from django.views.generic import View, TemplateView


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
