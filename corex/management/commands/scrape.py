"""
Scraping commands

"""
from collections import deque

from django.core.management.base import BaseCommand
from serbia.scrapers.companies import SerbiaCompanyScraper as Scc
from serbia.scrapers.officials import SerbiaOfficialsScraper as Sos
from serbia.scrapers.procurement import SerbiaProcurementScraper as Sps
from usa.procurement import FedContractsScraper as Fcs


class ScraperScheduler:
    """Schedule scraping tasks

    """
    def __init__(self):
        """Initiliaze task queue"""
        self._task_queue = deque()

    def scraping_task(self, task):
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
        sched.scraping_task(Fcs().run())
        sched.scraping_task(Sos().run())
        sched.scraping_task(Scc().run())
        sched.scraping_task(Sps().run())

        # run scheduler
        sched.run()
