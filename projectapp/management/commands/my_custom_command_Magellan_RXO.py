import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = 'https://rxoconnect.rxo.com/api/availableloads/search/loadboard'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': 'https://carrier.rxoconnect.rxo.com'
        }

        response = requests.post(url, headers=headers)
        print(response)
        print(response.status_code)
