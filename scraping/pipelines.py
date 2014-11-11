# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dateutil import parser

from django.db.utils import IntegrityError
from django.db.models.fields import DateField, DateTimeField
from scrapy import log

from veritza.apps.core.models import PublicOfficial


class VeritzaModelsPipeline(object):
    def process_item(self, item, spider):
        # check for and format datetime fields
        for field in item.django_model._meta.fields:
            if isinstance(field, (DateField, DateTimeField)) and field.name not in ('created', 'updated'):
                try:
                    formatted_date = parser.parse(item[field.name])
                    item[field.name] = formatted_date
                except (AttributeError, TypeError) as e:
                    item[field.name] = None

        # converting django item to django model instance
        instance = item.save()

        # saving the instance to the database
        if isinstance(instance, PublicOfficial):
            try:
                instance.save()
            except IntegrityError as e:
                log.msg(e, level=log.ERROR)
        else:
            instance.save()

        return item
