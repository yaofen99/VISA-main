from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


def send_to_telegram(message):  # Telegram bot

    apiToken = '5704612050:AAEIS4ZcP19CDgZ5-g3uNFxw64Dvsmn0HRA'
    chatID = '-819110848'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

x = 0
count = 1

driver.get("https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
           "%20de%20visa")

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//div[4]/button').click()

driver.implicitly_wait(20)
driver.find_element(By.CLASS_NAME, 'custom-control-label').click()

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

while True:

    try:
        elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//p[@class="lead fr-text mt-4 mb-3 text-center"]')))

        driver.get(
            "https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
            "%20de%20visa")
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH,
                            '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, '//button[@class ="btn btn-primary btn-md"]').click()

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH,
                            '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

    except:
        send_to_telegram(
            "Свободные места на визу Франция https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
            "%20de%20visa")
        driver.save_screenshot(f'WARNING!!!!!{count}.png')

    print(count)
    count = count + 1
