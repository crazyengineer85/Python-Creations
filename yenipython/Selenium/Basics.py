from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "https://github.com/"

driver.get(url)

time.sleep(2)
driver.maximize_window() # unutma önemli :)
print(driver.title)

time.sleep(10)
driver.close()
