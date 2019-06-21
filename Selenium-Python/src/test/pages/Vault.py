from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from test.utils.WijmoUtils import WijmoUtils
from test.locators.Locators import Locators

class Vault():
    def __init__(self, driver):
        self.driver = driver;
        self.pgCaption_label_xpath = Locators.vault_pgCaption_label_xpath
        self.addStock_button_xpath = Locators.vault_addStock_button_xpath

        # XPath of Exchange combo
        self.exchange_input_xpath = Locators.vault_exchange_input_xpath
        self.exchange_combo_xpath = Locators.vault_exchange_combo_xpath
        
        # XPath of Custodian
        self.cust_combo_xpath = "//wj-combo-box[@id='custodianId']//span[contains(@class,'wj-glyph-down')]"

        # XPath of Account combo
        self.clientID_input_xpath = "//input[@formcontrolname='clientId']"
        self.clientID_combo_xpath = "//wj-auto-complete[@id='clientId']//span[contains(@class,'wj-glyph-down')]"

        # XPath of Security combo
        self.security_input_xpath = "//input[@formcontrolname='securityId']"
        self.security_combo_xpath = "//wj-combo-box[@id='securityId']//span[contains(@class,'wj-glyph-down')]"

        # XPath of Qty input field
        self.qty_input_xpath = "//input[@formcontrolname='quantity']"

        # XPath of Remarks field
        self.remarks_input_xpath = "//textarea[@formcontrolname='remarks']"

        # XPath of Submit button
        self.save_btn_xpath = "//button[@id='btnSave']"

        # XPath success message
        #self.msg_pop_xpath = "//wj-popup[@class='green_dialog wj-control wj-content wj-popup wj-state-focused']//p[contains(text(),'Record Saved Successfully.')]"
        self.okBtn_pop_xpath = "//wj-popup[@class='green_dialog wj-control wj-content wj-popup wj-state-focused']//button[@class='btn btn-default wj-hide'][contains(text(),'Ok')]"

        # XPath of Type combo
        self.type_combo_xpath = "//wj-combo-box[@id='entryType']//span[contains(@class,'wj-glyph-down')]"

        #####################################3

    def verifyPgTitle(self):
        assert(self.driver.find_element_by_xpath(self.pgCaption_label_xpath)!=0),"Page is NOT loaded."

    def addStock(self):
        self.driver.find_element_by_xpath(self.addStock_button_xpath).click()

    ######################
    # Data Entry
    ######################

    def setData(self, security, account, qty):
        driver = self.driver
        utils = WijmoUtils (driver)
        #wait = WebDriverWait(driver, 20)
        #wait.until(ec.element_to_be_clickable((By.XPATH, self.exchange_combo_xpath)))

        # Setting GSE exchange
        utils.WijmoList(self.exchange_combo_xpath, "GSE")

        # Setting Custodians
        # utils.WijmoList(self.cust_combo_xpath, self.cust_item_xpath)

        # Setting Account
        utils.WijmoList(self.clientID_combo_xpath, account)

        # Setting Security
        utils.WijmoList(self.security_combo_xpath, security)

        # Setting Type
        utils.WijmoList(self.type_combo_xpath,"Deposit")

        # Setting Qty
        driver.find_element_by_xpath(self.qty_input_xpath).clear()
        driver.find_element_by_xpath(self.qty_input_xpath).send_keys(qty)

        # Setting Remarks
        driver.find_element_by_xpath(self.remarks_input_xpath).clear()
        driver.find_element_by_xpath(self.remarks_input_xpath).send_keys("Added through Selenium.")

        # Data validation before submission
        #self.validateData(security,account,qty)

        # Submit
        driver.find_element_by_xpath(self.save_btn_xpath).click()

        # Confirmation
        driver.find_element_by_xpath(self.okBtn_pop_xpath).click()



    ##############
    # Method to get data
    ##################3

    def getData(self):
        driver = self.driver
        print (driver.find_element_by_xpath(self.exchange_input_xpath).get_attribute('value'))
        print (driver.find_element_by_xpath(self.clientID_input_xpath).get_attribute ('value'))
        print(driver.find_element_by_xpath(self.security_input_xpath).get_attribute('value'))
        print(driver.find_element_by_xpath(self.qty_input_xpath).get_attribute('value'))

    ###############
    # method to validate the data Entry
    #############33
    def validateData(self,security, account, qty):
        driver = self.driver
        assert (driver.find_element_by_xpath(self.clientID_input_xpath).get_attribute ('value')== account), "Client mismatched."
        assert (driver.find_element_by_xpath(self.security_input_xpath).get_attribute('value')== security), "Security mismatched."

    ##############
    # Grid
    #############
