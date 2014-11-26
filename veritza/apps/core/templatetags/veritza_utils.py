from django import template
from django.db.models import get_app, get_models

register = template.Library()


@register.filter
def count_objects(model_name_verbose, app_label='core'):
    app = get_app(app_label)
    for model in get_models(app):
        if model._meta.verbose_name_plural == model_name_verbose:
            return model.objects.all().count()
            break
    return "-"
