from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "https://www.stanford.edu/"

driver.get(url)
print(driver.title)
time.sleep(10)
driver.maximize_window()
driver.save_screenshot("stanfordhome.png")

url="https://www.harvard.edu/"
driver.get(url)
print(driver.title)
driver.fullscreen_window()
driver.save_screenshot("harvardhome.png")
time.sleep(10)
driver.back()
if "Stanford" in driver.title:
    driver.fullscreen_window()
    driver.save_screenshot("StanfordBighome.png")
time.sleep(5)
driver.forward()
if "Harvard" in driver.title:
    driver.fullscreen_window()
    driver.save_screenshot("HarvardBighome.png")
driver.back()
time.sleep(5)
driver.fullscreen_window()
time.sleep(5)
driver.close()