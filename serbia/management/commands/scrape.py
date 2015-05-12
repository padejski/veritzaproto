"""
Scraping commands

"""

from django.core.management.base import BaseCommand
from serbia.companies import SerbiaCompanyScraper as Scc
from serbia.officials import SerbiaOfficialsScraper as Sos


class Command(BaseCommand):
    help = 'start scrapers'

    def handle(self, *args, **options):
        """run command"""
        Sos().run()
        Scc().run()
