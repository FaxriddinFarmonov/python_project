from projectapp.models import Load
from selenium.webdriver.chrome.service import Service
service = Service('C:\\Users\\User\\PycharmProjects\\chromedriver-win64\\chromedriver.exe')  # To'liq yo'lni ko'rsating
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import requests
from django.contrib.sites import requests
from django.core.management.base import BaseCommand

from projectapp.models import Load
from datetime import datetime

import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://brokeredloads.com/?hsCtaTracking=c0bb1298-4dc3-4e63-a016-dbe9c6bf8ba2%7C60f0694a-89ef-44cd-ba7c-2febd4baa21a"

        # WebDriver'ni o'rnating va sahifani yuklang
        driver = webdriver.Chrome()  # Chromedriver yuklang yoki foydalanadigan brauzer uchun mos WebDriver'ni tanlang
        driver.get(url)

        # Qidirish tugmasini topish va bosing
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cphMain2_btnSearch")))
        search_button.click()

        # Qidirish natijalarini kutish
        time.sleep(5)  # Qidirish natijalari uchun yetarli vaqtini tanlash

        # Yuklarni topish
        loads = driver.find_elements(By.CSS_SELECTOR, "tr.results__item")

        # Yuklarni ma'lumotlari to'plami
        results = []
        for load in loads:
            load_info = {
                "Pickup Window": load.find_element(By.CLASS_NAME, "results__item__date").text,
                "Load #": load.find_element(By.CLASS_NAME, "results__item__load").text,
                "Origin": load.find_element(By.CLASS_NAME, "results__item__origin").text,
                "Destination": load.find_element(By.CLASS_NAME, "results__item__destination").text,
                "Distance To Origin": load.find_element(By.CLASS_NAME, "results__item__orig_dist").text,
                "Distance to Destination": load.find_element(By.CLASS_NAME, "results__item__dest_dist").text,
                "Load Miles": load.find_element(By.CLASS_NAME, "results__item__distance").text,
                "Rate": load.find_element(By.CLASS_NAME, "results__item__rate").text,
                "Size": load.find_element(By.CLASS_NAME, "results__item__ltl").text,
                "Equipment": load.find_element(By.CLASS_NAME, "results__item__truck").text
            }
            results.append(load_info)

        # WebDriver'ni yopish
        driver.quit()
        for load in json.dumps(results, ensure_ascii=False, indent=4):
            Load.objects.create(
                name=None,  # Adjust this if you have a suitable value for the name field
                # origin=load['Origin'],
                destination=load['Destination'],
                length=int(load['Length']) if load['Length'].isdigit() else None,
                weight=int(load['Weight']) if load['Weight'].isdigit() else None,
                contact=load['Phone'],
                comment=load['Equipment'],
                # pickup_date=datetime.strptime(load['Ship Date']) if load['Ship Date'] else None,
                # published_date=datetime.now(),
                # updated_date=datetime.now(),

                # Add any other fields that need to be set here
                truck_status='pending',  # Default value, adjust as necessary
                # results_count=len(loads),
                # results_data=load
            )

        # JSON formatida qaytarish
        return json.dumps(results, ensure_ascii=False, indent=4)







from django.core.management.base import BaseCommand
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import json
from projectapp.models import Load  # Load modelini yuklang


# class Command(BaseCommand):
#     help = 'Fetches loads data from a URL and saves it to the Load model'
#
#     def add_arguments(self, parser):
#         parser.add_argument('url', type=str, help='URL to fetch loads data from')
#
#     def handle(self, *args, **options):
#          url = "https://brokeredloads.com/?hsCtaTracking=c0bb1298-4dc3-4e63-a016-dbe9c6bf8ba2%7C60f0694a-89ef-44cd-ba7c-2febd4baa21a"
#
#         # WebDriver'ni o'rnating va sahifani yuklang
#         driver = webdriver.Chrome()  # Chromedriver yuklang yoki foydalanadigan brauzer uchun mos WebDriver'ni tanlang
#         # driver.get(url)
#
#         # Qidirish tugmasini topish va bosing
#         search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cphMain2_btnSearch")))
#         search_button.click()
#
#         # Qidirish natijalarini kutish
#         time.sleep(10)  # Qidirish natijalari uchun yetarli vaqtini tanlash
#
#         # Yuklarni topish
#         loads = driver.find_elements(By.CSS_SELECTOR, "tr.results__item")
#
#         # Yuklarni ma'lumotlari to'plami
#         saved_loads = []
#         for load in loads:
#             load_info = {
#                 "origin": load.find_element(By.CLASS_NAME, "results__item__origin").text,
#                 "destination": load.find_element(By.CLASS_NAME, "results__item__destination").text,
#                 "distance": float(load.find_element(By.CLASS_NAME, "results__item__orig_dist").text.split()[0]),
#                 "length": int(load.find_element(By.CLASS_NAME, "results__item__distance").text.split()[0]),
#                 "price": float(
#                     load.find_element(By.CLASS_NAME, "results__item__rate").text.replace(",", "").replace("$", "")),
#                 "truck_status": "pending"  # Default status
#                 # Qolgan ma'lumotlarni kerakli xususiyatlar bo'yicha qo'shing
#             }
#             # Load modeliga yozish
#             load_obj = Load.objects.create(**load_info)
#             saved_loads.append(load_obj)
#
#         # WebDriver'ni yopish
#         driver.quit()
#
#         self.stdout.write(self.style.SUCCESS(f'Successfully fetched and saved loads from {url}'))
#
