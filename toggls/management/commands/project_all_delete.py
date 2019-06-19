from django.core.management.base import BaseCommand, CommandError
from toggls.models import Project

class Command(BaseCommand):
    help = 'Delete All Projects'

    def handle(self, *args, **options):
        # Remove Tasks & Projects
        Project.objects.all().delete()
        self.stdout.write("Successfully Deleted All Projects.")

