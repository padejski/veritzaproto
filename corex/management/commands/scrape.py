"""
Scraping commands

"""
# ============================================================================
# necessary imports
# ============================================================================
from itertools import chain
from collections import deque

from django.core.management.base import BaseCommand

from serbia.scrapers import serbia_scrapers
from usa.scrapers import usa_scrapers

# ============================================================================
# scrapers list
# ============================================================================
SCRAPERS = chain(serbia_scrapers, [])


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
                pass


class Command(BaseCommand):
    """Scraping Command"""
    help = 'start scrapers'

    def handle(self, *args, **options):
        """run command"""
        # initialize scheduler
        sched = ScraperScheduler()

        # add scraping tasks
        for scp in SCRAPERS:
            sched.add_task(scp().run())

        # run scheduler
        sched.run()
