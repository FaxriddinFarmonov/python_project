import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://www.amilfreight.com/public/carrier/GetTrailerMaster"
        Apikey = "3772f7d5-5480-4244-a8a9-8aee4a15f783scasc"

        headers = {
            "Apikey": Apikey,
        }

        response = requests.post(url, headers=headers)
        print(response)
        print(response.status_code)

        if response.status_code == 200:
            data = response.json()
            print(data)