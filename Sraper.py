import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper():
    options = webdriver.ChromeOptions()
    #change binary_location to match your browser location
    options.binary_location = r"/usr/bin/google-chrome-stable"
    executable_path = '/usr/bin/chromedriver'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=Scraper.executable_path, options=Scraper.options)

    def open(self, website_name):
        self.driver.get(website_name)


    def tearDown(self):
        self.driver.quit()
        print('Successful teardown')


if __name__ == '__main__':
    scraper = Scraper()
    scraper.open('https://www.reddit.com/r/wallpapers')

    scraper.tearDown()
