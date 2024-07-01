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
        print(response.json())
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            for item in data:
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
                    # destination=f"{item['dest']['city']}, {item['dest']['state']}",
                    dh_d=None,
                    distance=item['destination_zip'],
                    length=item['length'],
                    weight=item['weight'],
                    price=item['total_cost'],
                    suggested_price=None,
                    commodity=item['commodity'],
                    contact=item['customer_phone'],
                    contact_type=None,
                    comment=None,
                    ref_number=None,
                    truck_status=item['truck'],
                    results_count=len(item['stops']),
                    results_data=item['stops']
                )
                load.save()
