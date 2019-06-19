from django.core.management.base import BaseCommand, CommandError
from toggls.models import Task

class Command(BaseCommand):
    help = 'Delete All Tasks'

    def handle(self, *args, **options):
        # Remove Tasks & Projects
        Task.objects.all().delete()
        self.stdout.write("Successfully Deleted All Tasks.")

