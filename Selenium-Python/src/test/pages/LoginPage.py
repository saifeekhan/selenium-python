from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from test.locators.Locators import Locators

class LoginPage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.userid_text_name = Locators.userid_text_name
        self.password_text_name = Locators.password_text_name
        self.login_submit_xpath = Locators.login_submit_xpath

    def setData(self, uid, pwd):
        self.verifyTitle()
        
        self.driver.find_element_by_name(self.userid_text_name).clear()
        self.driver.find_element_by_name(self.userid_text_name).send_keys(uid)

        self.driver.find_element_by_name(self.password_text_name).clear()
        self.driver.find_element_by_name(self.password_text_name).send_keys(pwd)

        self.driver.find_element_by_xpath(self.login_submit_xpath).click()


    def verifyTitle(self):
        assert (self.driver.title =="Marlin by Infotech"), "Page title not found."

    def verifyLoginField(self):
        assert (self.driver.find_element_by_name(self.userid_text_name)!=0),"Login field not found."


