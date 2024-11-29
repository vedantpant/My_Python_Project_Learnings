import time
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "aurpantjikaiseho"
PASSWORD = 'sigma@123'
INSTAGRAM_URL = 'https://www.instagram.com/'


class InstaFollower:

    def __init__(self):
        self.modal = None
        self.save_login_prompt = None
        self.password = None
        self.username = None
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                   "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(options=chrome_option)

    def login(self):
        print("Instagram Login")
        self.driver.get("https://www.instagram.com/")

        time.sleep(10)

        self.username = self.driver.find_element(By.NAME, 'username')

        self.username.send_keys(USERNAME)

        time.sleep(5)

        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.send_keys(PASSWORD)
        self.password.send_keys(Keys.ENTER)

        time.sleep(10)

        self.save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if self.save_login_prompt:
            self.save_login_prompt.click()

    def find_followers(self, pop_up_window=None):
        self.driver.get("https://www.instagram.com/{}/".format(SIMILAR_ACCOUNT))
        time.sleep(5)

        # go to followers list
        try:
            followers_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
            )
            followers_link.click()
        except Exception as e:
            print("An error occurred:", e)
        time.sleep(3.4)

        # Wait for the followers list modal to appear
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        self.modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
            time.sleep(5)

    def follow(self):
        self.login()
        self.find_followers()
        print("instagram follow")
        time.sleep(5)

        # Find the follow buttons using a more generic approach
        follow_buttons = self.driver.find_elements(By.XPATH,
                                                  "//div[contains(text(), 'Follow')]")

        # Ensure buttons are found
        if not follow_buttons:
            print("No follow buttons found.")
            return

        # Click each follow button
        for button in follow_buttons:
            print("button_click")
            self.driver.execute_script("arguments[0].click();", button)  # JavaScript-based click
            time.sleep(2.5)

Instabot = InstaFollower()
Instabot.follow()
