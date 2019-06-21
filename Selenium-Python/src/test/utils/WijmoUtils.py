from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from test.locators.Locators import Locators
#import time
#import os

class WijmoUtils():
    def __init__(self,driver):
        self.driver = driver
        self.wj_dropdown_xpath = Locators.wj_dropdown_xpath

    # method to find and click the partial string in wijmo drop down list.
    def WijmoList(self, spin, item):
        wait = WebDriverWait (self.driver, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, spin)))
        self.driver.find_element_by_xpath(spin).click()

        wait.until(ec.text_to_be_present_in_element((By.XPATH,self.wj_dropdown_xpath),'Select'))
        drop_down_menu = self.driver.find_elements(By.XPATH,self.wj_dropdown_xpath)

        for element in drop_down_menu:
            self.visibleText = element.get_attribute("innerHTML")
            if  (self.visibleText.find(item) != -1):
                element.click()
                break
