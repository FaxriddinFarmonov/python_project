import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://tpx.transportpro.net/availablefreight/search?cid=1002&originAddress=&originCity=&originState=&originZip=&originLatitude=&originLongitude=&destAddress=&destCity=&destState=&destZip=&destLatitude=&destLongitude=&originAddressSearch=&originRadius=50&destAddressSearch=&destRadius=50&_=1719487211159"

        response = requests.get(url)
        data = response.json()
        print(response.status_code)
        print(data)
