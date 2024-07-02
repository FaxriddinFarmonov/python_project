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

        # JSON faylga saqlash
        with open('loads.json', 'w', encoding='utf-8') as f:
            json.dump(loads, f, ensure_ascii=False, indent=4)

        print(f"Scraped data saved to loads.json")
