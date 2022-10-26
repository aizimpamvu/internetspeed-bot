from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISED_DOWN = 10
PROMISED_UP = 5

TWITTER_EMAIL = "hallyizza200@gmail.com"
TWITTER_PASSWORD = "Haly1234%"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.speedtest.net/")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)


        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[1]')
        print("Hello")
        go_button.click()
        time.sleep(60)

        self.up = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        self.down = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        tweet_login = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]')
        tweet_login.send_keys(Keys.ENTER)

        time.sleep(3)
        base_window = driver.window_handles[0]
        tw_login_window = driver.window_handles[1]
        driver.switch_to.window(tw_login_window)

        other_count = self.driver.find_element(By.XPATH, '//*[@id="use-other"]/div[2]')
        other_count.click()

        email = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(5)

        next_button = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]')
        next_button.click()

        password = self.driver.find_element('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys(Keys.ENTER)

        time.sleep(30)

        driver.switch_to.window(base_window)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
