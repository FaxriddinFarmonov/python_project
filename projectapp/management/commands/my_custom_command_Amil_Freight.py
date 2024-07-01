#  bundan yuklar royhatini bermagan

import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    help = 'Customized admin command. Hi readers!'

    def handle(self, *args, **options):
        url = "https://www.amilfreight.com/public/carrier/getloads"
        api_key = "3772f7d5-5480-4244-a8a9-8aee4a15f783"

        headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }

        body = {
            "SortColumn": "Rate",
            "SortOrder": 2,
            "PageIndex": 0,
            "PageCount": 50
        }

        response = requests.post(url, headers=headers, json=body)
        print(response.status_code)
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            for item in data['Item']["Item1"]:
                load = Load(
                    name=item.get('id'),
                    published_date=datetime.now(),
                    updated_date=None,
                    created_date=datetime.now(),
                    # pickup_date=datetime.strptime(item['pickupDatetime'], '%Y-%m-%dT%H:%M'),
                    to_date=None,
                    age=None,
                    # dlv_date=datetime.strptime(item['deliveryDatetime'], '%Y-%m-%dT%H:%M'),
                    to_dlv_date=None,
                    # origin=f"{item['origin']['city']}, {item['origin']['state']}",
                    dh_o=None,
                    destination=item["Miles"],
                    dh_d=None,
                    distance=item['Miles'],
                    length=None,
                    weight=item['Weight'],
                    price=item['Salesrate'],
                    suggested_price=None,
                    commodity=item['Commodity'],
                    contact=None,
                    contact_type=None,
                    comment=None,
                    ref_number=None,
                    truck_status=None,
                    # results_count=len(item['stops']),
                    # results_data=item['stops']
                )
                load.save()
