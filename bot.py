import os
import time
from selenium import webdriver
import configparser

class InstagramBot:
    

    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.base_url='https://www.instagram.com'
        self.driver=webdriver.Chrome('chromedriver.exe')
        self.login()
        
        
        
        
    def login(self):
        self.driver.get('{}/accounts/login'.format(self.base_url))
        #self.driver.get('https://www.instagram.com/accounts/login/')
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

        time.sleep(2)
    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))
        
        
        
    def follow_user(self,user):
        self.nav_user(user)
        
        follow_button=self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        
        follow_button.click()
    
        
        
if __name__ == '__main__':
    config_path='./config.ini'
    cparser=configparser.ConfigParser()
    cparser.read(config_path)
    username=cparser['IG_AUTH']['USERNAME']
    password=cparser['IG_AUTH']['PASSWORD']
    
    ig_bot=InstagramBot(username,password)
    
    
    print(ig_bot.username)
    
    #ig_bot.nav_user('garyvee')
    ig_bot.follow_user('maddy_taneja')
