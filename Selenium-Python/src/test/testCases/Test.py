from test.pages.EnvironmentSetup import EnvironmentSetup
from test.pages.HomePage import HomePage
from test.pages.LoginPage import LoginPage
from test.pages.Vault import Vault

import time
import HtmlTestRunner
import unittest

class scenario_a (EnvironmentSetup):
    
    def test_01_login_valid(self):
        driver = self.driver
        excel = self.excel
        driver.get(self.conf.getBaseUrl())

        loginPg = LoginPage(driver)
        loginPg.setData(excel.getStringData('Login',2,2), excel.getStringData('Login',2,3))

    def test_03_verifyHomePage(self):
        homePg = HomePage(self.driver)
        homePg.verifyHomePg()

    def test_06_vault(self):
        driver = self.driver
        homePg = HomePage(driver)
        homePg.clickVault()

        vaultPg = Vault(driver)
        vaultPg.addStock()
        vaultPg.setData("ABL","0000000550680-LI/0","300")
        time.sleep(5)
        vaultPg.getData()

    def test_09_logout(self):
        driver = self.driver
        homePg = HomePage(driver)
        homePg.logOut()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/saif.khan/git/selenium-python/Selenium-Python/output/reports'))







