from githubuserinfo import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
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
    # def load_followers(self):
    #     item = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
    #     for i in item:
    #         self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary").text)
    def load_followers(self):
        usernames = self.browser.find_elements(
        By.CSS_SELECTOR,
        "a.Link--secondary"
        )

        for user in usernames:
            try:
                name = user.text
                if name and name not in self.followers:
                    self.followers.append(name)
            except StaleElementReferenceException:
                continue
    def get_followers(self):
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(2)
        
        while True:
            self.load_followers()

            try:
                next_button = self.browser.find_element(By.LINK_TEXT, "Next")
                next_button.click()
                time.sleep(2)
            except NoSuchElementException:
                print("Son sayfaya gelindi.")
                break
            # links = self.browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME,"a")

            # if len(links)==1:
            #     if links[0].text == "Next":
            #         links[0].click()
            #         time.sleep(1)
            #         self.load_followers()
            #     else:
            #         break
            # else: # Link değeri birden fazlaysa (a)

            #     for i in links:
            #         if i.text == "Next":
            #             i.click()
            #             time.sleep(1)
            #             self.load_followers()
            #         else:
            #             continue


#
github = Github(username,password)
github.SignIn()
github.get_followers()
print(len(github.followers))
print(github.followers)