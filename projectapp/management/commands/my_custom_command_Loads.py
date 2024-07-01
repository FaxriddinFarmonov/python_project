import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://loadboard.oregonlogistics.com/rest-api/loads-public?range=[0,50]&"


        response = requests.get(url)
        print(response)
        print(response.status_code)

        if response.status_code == 200:
            data = response.json()
            print(data)