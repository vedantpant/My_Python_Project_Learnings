import time
from telnetlib import EC

import requests as re
from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

url = "https://appbrewery.github.io/Zillow-Clone/"
page = re.get(url)

soup = BeautifulSoup(page.content, "html.parser")
list_of_prices = []
links_of_address = []
list_of_address = []
property_results = soup.find_all('li', 'ListItem-c11n-8-84-3-StyledListCardWrapper')
for result in property_results:

    price_list = result.find_all_next('span', 'PropertyCardWrapper__StyledPriceLine')
    for price in price_list:
        price_data = price.text.strip("/mo+ 1 bd")
        list_of_prices.append(price_data)

    address_link = result.find_all_next('a', 'property-card-link')
    for link in address_link:
        links_of_address.append(link["href"])

    address_list = result.find_all_next('address', {'data-test': 'property-card-addr'})
    for address in address_list:
        address_data = address.get_text().replace("|","")
        address_data = address_data.strip()
        list_of_address.append(address_data)


sheet_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeAUQJGAm0SUQP63fY8LGPtz_kTX9KJ1ABm4w3gdyQ6FyvB1Q/viewform?usp=sf_link'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
driver.get(sheet_url)

for price, address, link in zip(list_of_prices, list_of_address, links_of_address):

    time.sleep(2.5)
    address_info = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_info.send_keys(address)

    time.sleep(2.5)
    price_info = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_info.send_keys(price)

    time.sleep(2.5)
    link_info = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_info.send_keys(link)

    time.sleep(2.5)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(2.5)
    submit_another = driver.find_element(By.LINK_TEXT, 'Submit another response')
    submit_another.click()
