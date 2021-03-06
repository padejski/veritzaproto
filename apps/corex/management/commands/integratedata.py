"""
make data integrations

"""
# ============================================================================
# imports
# ============================================================================
from django.core.management.base import BaseCommand

from apps.serbia.integration import SerbiaIntegrator
from apps.usa.integration import UsaIntegrator

# ============================================================================
# data integration: django command
# ============================================================================
class Command(BaseCommand):
    """integration command

    """
    help = "perform data integrations"

    def handle(self, *args, **options):
        """."""
        print('perfoming data integrations')
        SerbiaIntegrator().run()
        UsaIntegrator().run()
# ============================================================================
# EOF
# ============================================================================
