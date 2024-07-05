# from models import Load
from selenium.webdriver.chrome.service import Service
service = Service('C:\\Users\\User\\PycharmProjects\\chromedriver-win64\\chromedriver.exe')  # To'liq yo'lni ko'rsating

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def scrape_load_details(url):
    # WebDriver o'rnatish
    service = Service(
        'C:\\Users\\User\\PycharmProjects\\chromedriver-win64\\chromedriver.exe')  # To'liq yo'lni ko'rsating

    options = Options()
    options.add_argument('--headless')  # Brauzerni o'rnatsa kerak, xususan headless rejimda
    driver = webdriver.Chrome(service=service, options=options)

    # Saytga kirish va ma'lumotlarni yig'ish
    driver.get(url)
    driver.implicitly_wait(10)  # 10 sekundga qadar kuting

    # Qidirish tugmasini topish va bosing
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cphMain2_btnSearch")))
    search_button.click()

    # Qidirish natijalarini kutish
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr[@class="results__more"]')))

    # Ma'lumotlarni yig'ish
    load_details_list = []
    try:
        loads = driver.find_elements(By.XPATH, '//tr[@class="results__more"]')
        print(loads[0].find_element(By.XPATH, './/td[contains(text(), "Phone:")]/following-sibling::td/a').get_attribute('href').replace('tel:', '').strip())
        for load in loads:
            load_details = {}
            load_number_elem = load.find_element(By.XPATH, './/td[contains(text(), "Load #:")]/following-sibling::td')
            load_miles_elem = load.find_element(By.XPATH, './/td[contains(text(), "Load Miles:")]/following-sibling::td')
            rate_elem = load.find_element(By.XPATH, './/td[contains(text(), "Rate:")]/following-sibling::td')
            contact_elem = load.find_element(By.XPATH, './/td[contains(text(), "Contact:")]/following-sibling::td')
            info_elem = load.find_element(By.XPATH, './/td[contains(text(), "Info:")]/following-sibling::td')
            phone_elem = load.find_element(By.XPATH, './/td[contains(text(), "Phone:")]/following-sibling::td/a')
            weekend_loading_elem = load.find_element(By.XPATH, './/td[contains(text(), "Weekend Loading:")]/following-sibling::td')

            # Ma'lumotlarni olish

            load_details['Load #'] = load_number_elem.get_attribute('textContent').strip()
            load_details['Load Miles'] = load_miles_elem.get_attribute('textContent').strip()
            load_details['Rate'] = rate_elem.get_attribute('textContent').strip()
            load_details['Contact'] = contact_elem.get_attribute('textContent').strip()
            load_details['Info'] = info_elem.get_attribute('textContent').strip()
            load_details['Phone'] = phone_elem.get_attribute('href').replace('tel:', '').strip() if phone_elem else ''
            load_details['Weekend Loading'] = weekend_loading_elem.get_attribute('textContent').strip()

            load_details_list.append(load_details)

    except Exception as e:
        print(f"Xatolik yuz berdi: {str(e)}")

    # WebDriver ni yopish
    driver.quit()

    return load_details_list

# Test qilish
url = 'https://brokeredloads.com/?hsCtaTracking=c0bb1298-4dc3-4e63-a016-dbe9c6bf8ba2%7C60f0694a-89ef-44cd-ba7c-2febd4baa21a'
load_details_list = scrape_load_details(url)
print(json.dumps(load_details_list, indent=2))


