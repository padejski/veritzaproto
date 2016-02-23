"""
Scraping commands

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
SCRAPERS = chain(serbia_scrapers, usa_scrapers)


class ScraperScheduler:
    """Schedule scraping tasks

    """
    def __init__(self):
        """Initiliaze task queue"""
        self._task_queue = deque()

    def add_task(self, task):
        """Admit a newly started task to the scheduler

        """
        self._task_queue.append(task)

    def run(self):
        """Execute unit there are no more tasks

        """
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                continue
            except Exception as exc:
                print(exc)
                continue


class Command(BaseCommand):
    """Scraping Command"""
    help = 'start scrapers'

    def add_arguments(self, parser):
        """take optional positional arguments"""
        parser.add_argument("-s", "--scraper", dest='scraper', type=str, help="scraper's name")

    def handle(self, *args, **options):
        """run command"""
        scrapers = SCRAPERS

        if options['scraper']:
            scrapers = [s for s in SCRAPERS if s.NAME == options['scraper']]

        # initialize scheduler
        sched = ScraperScheduler()

        # add scraping tasks
        for scp in scrapers:
            tracker = ScrapeTracker.objects.filter(name=scp.NAME).first()
            tracker.last_run = datetime.now()
            tracker.status = 'running'
            tracker.save()

            sched.add_task(scp().run())

        # run scheduler
        try:
            sched.run()

            for scp in scrapers:
                tracker = ScrapeTracker.objects.filter(name=scp.NAME).first()
                tracker.status = 'finished'
                tracker.save()
        except KeyboardInterrupt:
            print('quitting...\n')
            sys.exit(0)
