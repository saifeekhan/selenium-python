from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginPage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.userid_textbox_name = "email"
        self.password_textbox_name = "password"
        self.login_button_xpath="//button[@class='login_btn']"

    def setData(self, id, pwd):
        self.verifyTitle()
        # R&D
        # print ("Login Form")
        # print (len(self.driver.find_elements(By.NAME,self.userid_textbox_name)))
        ####
        self.driver.find_element_by_name(self.userid_textbox_name).clear()
        self.driver.find_element_by_name(self.userid_textbox_name).send_keys(id)

        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)

        self.driver.find_element_by_xpath(self.login_button_xpath).click()


    def verifyTitle(self):
        assert (self.driver.title =="Marlin by Infotech"), "Page title not found."

    def verifyLoginField(self):
        assert (self.driver.find_element_by_name(self.userid_textbox_name)!=0),"Login field not found."


