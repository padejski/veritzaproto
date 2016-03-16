"""
Utility command for testing scraper

"""
import sys

from django.core.management.base import BaseCommand

from apps.usa.scrapers import FinDisclosuresScraper as scraper


class Command(BaseCommand):
    """Scraping Command"""
    help = 'start scrapers'

    def handle(self, *args, **options):
        """run command"""
        try:
            for _ in scraper().run():
                pass
        except KeyboardInterrupt:
            sys.exit(0)
