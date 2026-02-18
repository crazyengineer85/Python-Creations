from selenium import webdriver
import time


"""


Firefox (geckodriver) Selenium oturumu bitse bile tarayıcıyı her zaman anında öldürmez.
Chrome ise çok daha agresif davranır.
"""
# driver = webdriver.Firefox()

driver = webdriver.Chrome()
url = "https://stanford.edu"

driver.get(url)




# time.sleep(60)

input("kapatmak için Enter'a bas.....")




