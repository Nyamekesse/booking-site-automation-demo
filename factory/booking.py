import os

from selenium import webdriver

from config import URL


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium-chrome-drivers\chromedriver_win32"):
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()

    def get_page(self):
        self.get(URL)
