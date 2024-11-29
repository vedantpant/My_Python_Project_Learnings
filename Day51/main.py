from selenium.webdriver import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TWITTER_EMAIL = 'aurpantkaiseho'
TWITTER_PASSWORD = 'contrasena@123'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.post_button = None
        self.up_speed = None
        self.down_speed = None
        self.tweet = None
        self.log_in_button = None
        self.password = None
        self.username_button = None
        self.sign_in_button = None
        self.download_speed = None
        self.upload_speed = None
        self.go_button = None
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                   "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(options=chrome_option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        print("internet_speed:")
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        self.go_button.click()

        self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div['
                                                                 '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                 '1]/div[1]/div/div[2]/span')
        self.upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div['
                                                               '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                               '1]/div[2]/div/div[2]/span')

        time.sleep(80)
        self.down_speed = self.download_speed.text
        self.up_speed = self.upload_speed.text
        return self.down_speed, self.up_speed

    def tweet_at_provider(self):
        print("tweet provider.")
        self.driver.get("https://x.com/")

        time.sleep(10)

        self.sign_in_button = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        self.sign_in_button.click()

        time.sleep(10)

        self.username_button = self.driver.find_element(By.NAME, 'text')
        self.username_button.send_keys(TWITTER_EMAIL)
        self.username_button.send_keys(Keys.ENTER)

        time.sleep(10)

        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.send_keys(TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)

        time.sleep(10)

        self.tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                        'div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/'
                                                        'div/'
                                                        'div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/'
                                                        'div/'
                                                        'div/div[2]/div/div/div/div')
        self.tweet.send_keys(f'hey internet provider what is up with my internet speed upload_speed:{self.up_speed} '
                             f'and download_speed: {self.down_speed}. '
                             f'While I am paying down speed: 1000mbps and up speed as 150mbps')

        self.post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                              'div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/'
                                                              'div[2]/div[2]/div[2]/div/div/div/button')

        self.post_button.click()


Internet_Speed = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

Internet_Speed.get_internet_speed()
Internet_Speed.tweet_at_provider()
