import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://raptorcp5.edgetms.com/api/index.cfm/v1/boards/shipments?page=1&limit=5000"

        token = "Bearer 8fafeccd-75a8-11ec-aa95-1418775a4a62"


        headers = {
            "Authorization": token,
        }

        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.json())
