"""
scrapers set up command

"""
# ============================================================================
# necessary imports
# ============================================================================
import sys
from itertools import chain
from collections import deque
from datetime import datetime

from django.core.management.base import BaseCommand

from apps.serbia.scrapers import serbia_scrapers
from apps.usa.scrapers import usa_scrapers
from apps.corex.models import ScrapeTracker

# ============================================================================
# scrapers list
# ============================================================================
SCRAPERS = [scp.NAME for scp in chain(serbia_scrapers, usa_scrapers)]
MONTE_SCRAPERS = ['montenegro:companies', 'montenegro:procurements',
                  'montenegro:public-officials']


class Command(BaseCommand):
    """Scraping Command"""
    help = 'initialize scrapers by setting up tracking database entries'

    def handle(self, *args, **options):
        """run command"""
        for scp in chain(SCRAPERS, MONTE_SCRAPERS):
            exists = ScrapeTracker.objects.filter(name=scp).first()
            if not exists:
                tracker = ScrapeTracker(name=scp)
                tracker.save()
                print('initialized {}'.format(scp))
