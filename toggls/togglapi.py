import requests
from datetime import date
from datetime import datetime as dt
from datetime import timedelta as td

API_TOKEN = '91076e0b1a468c5db58076e72893043a'
W_ID = '3265483'
MAIL = 'taishi2060@gmail.com'
API_Endpoint = 'https://toggl.com/reports/api/v2/details'

# API_TOKEN = os.environ["Toggl_API_TOKEN"]
# W_ID = os.environ["Toggl_WORKSPACE_ID"]
# MAIL = os.environ["MAIL"]

class TogglAPI:
    def __init__(self, since_date=dt.now().strftime('%Y-%m-%d'), until_date=dt.now().strftime('%Y-%m-%d')):
        headers = {'content-type': 'application/json'}
        today = date.today().isoformat()
        auth = requests.auth.HTTPBasicAuth(API_TOKEN, 'api_token')
        params = {'workspace_id': W_ID,
                  'user_agent': MAIL,
                  'since': since_date,
                  'until': until_date
                  }
        current = requests.get(API_Endpoint, auth=auth, headers=headers, params=params)
        current_json = current.json()
        self.data = current_json['data']

    def get(self):
        return self.data

