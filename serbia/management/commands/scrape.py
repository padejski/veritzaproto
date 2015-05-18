"""
Scraping commands

"""

from django.core.management.base import BaseCommand
from serbia.companies import SerbiaCompanyScraper as Scc
from serbia.officials import SerbiaOfficialsScraper as Sos
from usa.procurement import FedContractsScraper as Fcs


class Command(BaseCommand):
    help = 'start scrapers'

    def handle(self, *args, **options):
        """run command"""
        Fcs().run()
        # Sos().run()
        # Scc().run()
