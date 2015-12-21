from optparse import make_option

from django.core.management.base import BaseCommand

from apps.core.models import refresh_all_veritzas


class Command(BaseCommand):

    help = 'Refresh all Veritzas'

    option_list = BaseCommand.option_list + (
        make_option('--delete-old',
            action='store_true',
            dest='delete_old',
            default=False,
            help='Delete all old records before creating the new ones'),
    )

    def handle(self, *args, **options):
        refresh_all_veritzas(delete_old=options['delete_old'])
