import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import json

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://wila.aljex.com/proute.php"
        params = {
            "qual": "58fghh65",
            "type": "lookup",
            "prcnam": "availloads",
            "B1": "View Available Loads"
            # date, ostate va boshqa zarur parametrlarni qo'shishingiz mumkin
        }
        html_content = requests.post(url,params=params)

    def parse_html_to_json(html_content):
        # HTML ni BeautifulSoup orqali qayta ishlab chiqamiz
        soup = BeautifulSoup(html_content, 'html.parser')

        # JSON obyektini tuzamiz
        data = {}

        # Ma'lumotlarni tanlash
        data['title'] = soup.title.text.strip()
        data['content'] = soup.find(id='content').get_text().strip()
        items = soup.find_all('li')
        data['items'] = [item.text.strip() for item in items]

        # JSON formatiga o'tkazamiz
        json_data = json.dumps(data, indent=4)
        return json_data

        # HTML ma'lumotlarni olish

    html_content = """
       <!DOCTYPE html>
       <html>
       <head>
           <title>Sample HTML Page</title>
       </head>
       <body>
           <div id="content">
               <h1>Hello, World!</h1>
               <p>This is a sample HTML content.</p>
               <ul>
                   <li>Item 1</li>
                   <li>Item 2</li>
                   <li>Item 3</li>
               </ul>
           </div>
       </body>
       </html>
       """

    # HTML ni JSON formatiga o'tkazish
    json_data = parse_html_to_json(html_content)
    print(json_data)