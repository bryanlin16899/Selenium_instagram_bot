from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "caseyneistat"
USERNAME = "bryan16899"
PASSWORD = "hygnjutbm03"

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(url="https://www.instagram.com/")
        sleep(3)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        sleep(2)

        pop_up = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            sleep(2)
            print("2")

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
                cancel_button.click()

Bot = InstaFollower(CHROME_DRIVER_PATH)
Bot.login()
Bot.find_followers()
Bot.follow()
