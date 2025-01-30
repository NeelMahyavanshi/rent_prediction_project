from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DriverManager:
    def __init__(self):
        self.driver = self._initialize_webdriver()

    def _initialize_webdriver(self):
        # Initialize web driver
        service = Service(ChromeDriverManager().install()) #Automatically downloads the functions
        return webdriver.Chrome(service=service)
    
    def navigate_to_page(self, url):
        # opening the url in the webdriver
        self.driver.get(f"{url}")
    
    def close_driver(self):
        # Closing the driver
        self.driver.quit()

class 