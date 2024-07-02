# from django.shortcuts import render
# from projectapp.models import Book
# # Create your views here.

from bs4 import BeautifulSoup
import requests
payload = {
        'qual': '58fghh65',
        'type': 'lookup',
        'prcnam': 'availloads',
        'date': '',
        'ostate': '',
        'B1': 'View Available Loads'
    }
url = 'https://wila.aljex.com/proute.php'
req = requests.post(url,data=payload)
print(req.text)



