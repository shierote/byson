from django.core.management.base import BaseCommand, CommandError
from toggls.models import Task, Project
from datetime import date
from datetime import datetime as dt
from datetime import timedelta as td
import re
from toggls import togglapi as ta

pattern = '(\d*)min\/'

class Command(BaseCommand):
    help = 'Importing tracking data from Toggl, using Toggl API'
    def add_arguments(self, parser):
        parser.add_argument(
                'import_until_date', 
                default=(dt.now() - td(days=7)).strftime('%Y-%m-%d'),
                nargs='+', 
                type=str
                )

    def handle(self, *args, **options):
        # Recreate Tasks & Projects
        target_date = dt.now() + td(days=1)
        target_date_str = target_date.strftime('%Y-%m-%d')
        import_until_date = options['import_until_date'][0] 

        self.stdout.write('Start Importing')
        self.stdout.write('Finish date', ending=': ')
        self.stdout.write(import_until_date)
        self.stdout.write('')

        while target_date_str != import_until_date:
            target_date -= td(days=1)
            target_date_str = target_date.strftime('%Y-%m-%d')
            self.stdout.write(target_date_str)

            toggl_data = ta.TogglAPI(since_date=target_date_str, until_date=target_date_str).get()
            
            for task in toggl_data:

                expected_dur_match = re.match(pattern, task['description'])
                expected_dur = int(expected_dur_match[1])*60 if expected_dur_match else None
                if Project.objects.filter(project=task['project']):
                    p = Project.objects.filter(pid=task['pid'])[0]
                    p.task_set.all()

                    if not(Task.objects.filter(start=task['start'])):
                        t = p.task_set.create(description=task['description'], start=task['start'],
                            end=task['end'], dur=task['dur']//1000, expected_dur=expected_dur, pid=task['pid'])
                        t.save()
                        self.stdout.write(t.description)

                elif task['project'] == None:
                    if not(Task.objects.filter(start=task['start'])):
                        t = Task(description=task['description'], start=task['start'],
                            end=task['end'], dur=task['dur']//1000, expected_dur=expected_dur, pid=task['pid']
                            )
                        t.save()
                        self.stdout.write(t.description)
                else:
                    p = Project(pid=task['pid'], project=task['project'], project_hex_color=task['project_hex_color'])
                    p.save()

                    if not(Task.objects.filter(start=task['start'])):
                        t = p.task_set.create(description=task['description'], start=task['start'],
                            end=task['end'], dur=task['dur']//1000, expected_dur=expected_dur, pid=task['pid'])
                        t.save()
                        self.stdout.write(t.description)

            self.stdout.write("\n\n")
        self.stdout.write("Successfully Updated Toggl Data.")

