
# Data we need : 
# Rent, 
# Bath, Bed, Sqaure ft, Street number, Street name, postal code, neighboorhood, property type, description(furnished?, parking?, pool?, heating included?, electricity included?, washer and dryer included?), 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from backend.app.utils.logger import app_logger
import numpy as np


class ListingScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self._initialize_driver()
        app_logger.info(f"Initialized ListingScraper for URL : {self.url}")
        self.driver.get(self.url)

    def _initialize_driver(self):
        # Initialize Chrome driver
        app_logger.info(f"Initializing the Chrome Driver")
        service = Service(ChromeDriverManager().install())  # Automatic management of ChromeDriver
        return webdriver.Chrome(service=service)
    def scrape_lisiting(self):
        # Scraping all the data and making a dictionary
        app_logger.info(f"Starting to scrape the listing data")
        data = {
            "title": self._get_title(),
            "house_type": self._get_house_type(),
            "address": self._get_address(),
            "images": self._get_images(),
            "bedrooms": self._get_bedrooms(),
            "price": self._get_price(),
            "bath": self._get_bath(),
            "size": self._get_size(),
            "description": self._get_description(),
        }
        app_logger.info(f"Finished scraping the data")
        return data
    
    def _get_title(self):
        # Scrape the title of the listing
        app_logger.info(f"Scraping the title")
        try:
            title = self.driver.find_element(By.CSS_SELECTOR, "li.breadcrumb__item--active span[itemprop='name']").text
            app_logger.info(f"Title scraped : {title}")
            return title
        except Exception as e:
            app_logger.error(f"Error scraping title : {e}")
            return np.nan
        
    def _get_house_type(self):
        # Scrape the house type of the listing
        app_logger.info(f"Scraping the house type of the listing")
        try:
            house_type = self.driver.find_element(By.CSS_SELECTOR, "ul.listing-card-bar__descriptor > li:nth-child(2)").text
            app_logger.info(f"House type scraped : {house_type}")
            return house_type
        except Exception as e:
            app_logger.error(f"Error scraping house type : {e}")
            return np.nan
        


