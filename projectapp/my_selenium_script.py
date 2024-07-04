from models import Load
from selenium.webdriver.chrome.service import Service
service = Service('C:\\Users\\User\\PycharmProjects\\chromedriver-win64\\chromedriver.exe')  # To'liq yo'lni ko'rsating
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def fetch_loads_data(url):
    # WebDriver'ni o'rnating va sahifani yuklang
    driver = webdriver.Chrome()  # Chromedriver yuklang yoki foydalanadigan brauzer uchun mos WebDriver'ni tanlang
    driver.get(url)

    # Qidirish tugmasini topish va bosing
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cphMain2_btnSearch")))
    search_button.click()

    # Qidirish natijalarini kutish
    time.sleep(10)  # Qidirish natijalari uchun yetarli vaqtini tanlash

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

    # JSON formatida qaytarish
    return json.dumps(results, ensure_ascii=False, indent=4)

# Test qilish
url = "https://brokeredloads.com/?hsCtaTracking=c0bb1298-4dc3-4e63-a016-dbe9c6bf8ba2%7C60f0694a-89ef-44cd-ba7c-2febd4baa21a"
loads_data = fetch_loads_data(url)

