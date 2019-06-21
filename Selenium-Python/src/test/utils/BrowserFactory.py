from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from test.utils.ConfigDataProvider import ConfigDataProvider


class BrowserFactory():
    driver: WebDriver
    conf: ConfigDataProvider

    def startApplication(self, brw):
        
        
        if brw=="Chrome":
            driver = webdriver.Chrome(executable_path="C:/Users/saif.khan/PycharmProjects/MyFramework/Drivers/chromedriver.exe")
        elif brw == "Firefox":
            driver = webdriver.Firefox()

        driver.implicitly_wait(20)
        driver.maximize_window()

        return driver
    