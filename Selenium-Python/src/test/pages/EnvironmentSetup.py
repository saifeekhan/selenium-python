import unittest
from test.utils.BrowserFactory import BrowserFactory
from test.utils.ExcelDataProvider import ExcelDataProvider
from test.utils.ConfigDataProvider import ConfigDataProvider
from selenium import webdriver
from test.utils.CommonUtils import CommonUtils

class EnvironmentSetup(unittest.TestCase):
    driver: webdriver
    excel: ExcelDataProvider
    conf: ConfigDataProvider
    cUtils: CommonUtils

    @classmethod
    def setUpClass(cls):
        bf = BrowserFactory()
        cls.excel = ExcelDataProvider()
        cls.conf = ConfigDataProvider()
        cls.cUtils = CommonUtils ()
        cls.driver = bf.startApplication(cls.conf.getBrowser())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
