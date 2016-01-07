from django import template
from django.db.models import get_app, get_models

from apps.corex.models import ScrapeTracker

register = template.Library()


@register.filter
def count_objects(model_name_verbose, app_label='core'):
    app = get_app(app_label)
    for model in get_models(app):
        if model._meta.verbose_name_plural == model_name_verbose:
            return model.objects.all().count()
            break
    return "-"

@register.filter
def is_subscribed(user, dataset, app_label='core'):
	return user.is_subscribed(dataset, app_label)

@register.filter
def is_running(scraper):
    status = ScrapeTracker.objects.filter(name=scraper).first().status
    if status == 'running':
        return True
    return False

@register.filter
def is_pending(scraper):
    status = ScrapeTracker.objects.filter(name=scraper).first().status
    if status == 'pending':
        return True
    return False

@register.filter
def split_pick_first(strvar, sep=','):
    return strvar.split(sep)[0]
