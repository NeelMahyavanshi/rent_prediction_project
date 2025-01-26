
# Data we need : 
# Rent, 
# Bath, Bed, Sqaure ft, Street number, Street name, postal code, neighboorhood, property type, description(furnished?, parking?, pool?, heating included?, electricity included?, washer and dryer included?), 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize ChromeDriver
driver = webdriver.Chrome()  # Update with the correct path if needed

# Automate a website
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# Close the browser
driver.quit()




