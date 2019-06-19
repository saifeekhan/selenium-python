from test.pages.Vault import Vault
class HomePage():
    # Constructor
    def __init__(self, driver):
        self.driver = driver;
        self.ripple_menu_xpath = "//span[@class='ripple']"
        self.settings_link_xpath = "//i[@class='fa fa-cog fa-lg']"
        self.logout_link_xpath="// a[contains(text(), 'Log Out')]"

        self.vault_menu_xpath = "//a[contains(text(),'Vault')]"
        self.vault_subMenu_xpath="//a[contains(text(),'Stock Deposit/Withdraw')]"

    def verifyHomePg(self):
        assert(self.driver.find_element_by_xpath(self.ripple_menu_xpath)!=0),"Home Page not loaded."

    def logOut(self):
        self.driver.find_element_by_xpath(self.settings_link_xpath).click()
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()

    def clickVault(self):
        driver = self.driver
        driver.find_element_by_xpath (self.vault_menu_xpath).click()
        driver.find_element_by_xpath(self.vault_subMenu_xpath).click()
        vaultPg = Vault(driver)
        vaultPg.verifyPgTitle()


