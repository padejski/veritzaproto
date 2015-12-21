from subprocess import call
from optparse import make_option
from django.core.management.base import BaseCommand
from apps.core.models import refresh_all_veritzas


class Command(BaseCommand):

    help = 'Run specific scraper'

    option_list = BaseCommand.option_list + (
        make_option('--delete-old',
            action='store_true',
            dest='delete_old',
            default=False,
            help='Delete all old records before creating the new ones'),
    )

    def handle(self, scraper, *args, **options):
        call(['scrapy', 'crawl', scraper])
