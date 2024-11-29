from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys("Vedant", Keys.ENTER)
last_name = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
last_name.send_keys("Pant", Keys.ENTER)
email_address = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email_address.send_keys("vedantpant@gmail.com", Keys.ENTER)
button_press = driver.find_element(By.XPATH, value='/html/body/form/button')
button_press.click()
