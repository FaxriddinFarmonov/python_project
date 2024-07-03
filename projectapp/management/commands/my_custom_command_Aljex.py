import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import json

from projectapp.models import Load
from datetime import datetime

import requests

import requests
from bs4 import BeautifulSoup
import json
from django.core.management.base import BaseCommand
from projectapp.models import Load

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        payload = {
            'qual': '58fghh65',
            'type': 'lookup',
            'prcnam': 'availloads',
            'date': '',
            'ostate': '',
            'B1': 'View Available Loads'
        }
        url = 'https://wila.aljex.com/proute.php'
        req = requests.post(url, data=payload)

        # Sahifani pars qilish
        soup = BeautifulSoup(req.text, 'html.parser')

        # Ma'lumotlarni ajratish
        loads = []
        for row in soup.select('tr'):  # Jadval qatorlarini topish
            columns = row.find_all('td')
            if len(columns) >= 8:  # Kerakli ustunlar soni bo'lsa
                load_data = {
                    'Ship Date': columns[0].get_text(strip=True),
                    'Origin': columns[1].get_text(strip=True),
                    'Destination': columns[2].get_text(strip=True),
                    'Trailer Type': columns[3].get_text(strip=True),
                    'Length': columns[4].get_text(strip=True),
                    'Weight': columns[5].get_text(strip=True),
                    'Phone': columns[6].get_text(strip=True),
                    'Office': columns[7].get_text(strip=True)
                }
                loads.append(load_data)

        for load in loads:
            Load.objects.create(
                name=None,  # Adjust this if you have a suitable value for the name field
                origin=load['Origin'],
                destination=load['Destination'],
                length=int(load['Length']) if load['Length'].isdigit() else None,
                weight=int(load['Weight']) if load['Weight'].isdigit() else None,
                contact=load['Phone'],
                comment=load['Office'],
                # pickup_date=datetime.strptime(load['Ship Date']) if load['Ship Date'] else None,
                # published_date=datetime.now(),
                # updated_date=datetime.now(),
                created_date=load["Ship Date"],
                # Add any other fields that need to be set here
                truck_status='pending',  # Default value, adjust as necessary
                # results_count=len(loads),
                results_data=load
            )