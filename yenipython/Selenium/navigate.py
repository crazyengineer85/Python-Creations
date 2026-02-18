from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


url = "https://github.com/search"
driver.get(url)
searchInput = driver.find_element(By.CLASS_NAME,"prc-components-Input-IwWrt")

time .sleep(2)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(5)
x = driver.find_elements(By.CSS_SELECTOR, ".Box-sc-62in7e-0 h3 a" )
count = 0
for i in x:
    count+=1
    print(f"{count} - {i.text}")
time.sleep(5)
driver.close()
"""

search sayfasının source'unu getirir
x = driver.page_source
print(x)

"""
"""
x = driver.find_elements(By.CSS_SELECTOR, ".Box-sc-62in7e-0 h3 a" )
for i in x:
    print(i.text)


Bu kod tüm başlıkları alır, link olarak gördüğünden li lewrin ortak class isimleri, h3 etiketi, a'nın text'ine
 kadar inmemiz gerekir
"""