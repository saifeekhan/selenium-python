from test.pages.Vault import Vault
from test.locators.Locators import Locators
class HomePage():
    # Constructor
    def __init__(self, driver):
        self.driver = driver;
        self.settings_link_xpath = Locators.settings_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath
        self.logo_img_xpath = Locators.logo_img_xpath

        self.vault_menu_xpath = Locators.vault_menu_xpath
        self.vault_subMenu_xpath = Locators.vault_subMenu_xpath

    def verifyHomePg(self):
        assert(self.driver.find_element_by_xpath(self.logo_img_xpath)!=0), "Home Page not loaded."

    def logOut(self):
        self.driver.find_element_by_xpath(self.settings_link_xpath).click()
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()

    def clickVault(self):
        driver = self.driver
        driver.find_element_by_xpath (self.vault_menu_xpath).click()
        driver.find_element_by_xpath(self.vault_subMenu_xpath).click()
        vaultPg = Vault(driver)
        vaultPg.verifyPgTitle()


