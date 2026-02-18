from githubuserinfo import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def SignIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(5)
        # 1. yol
        # self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        # self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        # self.browser.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[2]/form/div[3]/input").click()

        # 2. yol
        self.browser.find_element(By.ID, "login_field").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.NAME, "commit").click()
        time.sleep(2) 
    def get_followers(self):
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(2)
        item = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        for i in item:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary").text)
        # osman = self.browser.find_element(By.CSS_SELECTOR,".Link--secondary").text
        # if osman == "osmanpurcak":
        #     self.get_continue_followers()
        #     time.sleep(2)
        
        
    # Bu sadık turanın follower listesindeki bir adam seçilerek onun takip listesini almak
    # def get_contiue_followers(self):
    #     self.browser.get("https://github.com/osmanpurcak?tab=followers")
    #     items2 = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
    #     time.sleep(2)
    #     for i in items2:
    #         self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary").text)


github = Github(username,password)
github.SignIn()
github.get_followers()
# github.get_contiue_followers()
print(github.followers)