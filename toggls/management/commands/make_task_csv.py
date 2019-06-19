from django.core.management.base import BaseCommand, CommandError
from toggls.models import Task, Project
from datetime import date
from datetime import datetime as dt
from datetime import timedelta as td
import re
from toggls import togglapi as ta
import csv
import pandas as pd

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

        data_list = []

        while target_date_str != import_until_date:
            target_date -= td(days=1)
            target_date_str = target_date.strftime('%Y-%m-%d')
            self.stdout.write(target_date_str)

            toggl_data = ta.TogglAPI(since_date=target_date_str, until_date=target_date_str).get()
            for task in toggl_data:
                expected_dur_match = re.match(pattern, task['description'])
                expected_dur = int(expected_dur_match[1])*60 if expected_dur_match else None
                data_list.append([task['description'], task['project'], task['dur']//1000, expected_dur, task['start'], task['end'], task['project_hex_color']])
        columns = ['description', 'project', 'duration', 'expected_duration', 'started_at', 'ended_at', 'project_hex_color']
        df = pd.DataFrame(data_list ,columns=columns)
        df.to_csv('toggl_tasks.csv')
        self.stdout.write("Successfully Create CSV Data.")

