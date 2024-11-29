from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://tinder.com/")

email_address = "vedantpant@gmail.com"
password = "Sigma@123"

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Log in']")))
log_in.click()

time.sleep(5)

# Locate the "Log in with Facebook" button by its aria-label and click it
facebook_button = driver.find_element(By.XPATH, "//button[@aria-label='Log in with Facebook']")
facebook_button.click()

time.sleep(10)

base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

print(driver.title)

time.sleep(4)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("vedantpant.python@gmail.com")

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys("contrasena@123")
password_input.send_keys(Keys.ENTER)

input("Press manual prompt to enter....")

time.sleep(5)
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_button = driver.find_element(By.CLASS_NAME, "c1p6lbu0")
allow_button.click()

# Use WebDriverWait to wait for the button to be clickable
button_notification = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='I’ll miss out']"))
)

# Click the button
button_notification.click()
print("Button clicked successfully!")

button_accept = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='I accept']"))
)

# Click the button
button_accept.click()
print("Button clicked successfully!")

# Add an implicit wait (optional but helps ensure the page loads properly)
driver.implicitly_wait(10)

while True:
    print("called")
    like_button = driver.find_element(By.XPATH, '//button//span[text()="Like"]')
    driver.execute_script("arguments[0].click();", like_button)
    time.sleep(4)

