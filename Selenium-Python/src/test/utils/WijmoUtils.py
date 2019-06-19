from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import os

class WijmoUtils():
    def __init__(self,driver):
        self.driver = driver

    def WijmoList(self, spin, item):
        wait = WebDriverWait (self.driver, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, spin)))
        self.driver.find_element_by_xpath(spin).click()

        wait.until(ec.text_to_be_present_in_element((By.XPATH,"//div[@wj-part='dropdown']//div"),'Select'))
        drop_down_menu = self.driver.find_elements(By.XPATH,"//div[@wj-part='dropdown']//div")

        for element in drop_down_menu:
            if element.get_attribute("innerHTML") == item:
                element.click()
                break
