'''
Created on Jun 19, 2019
 
@author: saif.khan
'''
from test.pages.EnvironmentSetup import EnvironmentSetup

 
class tester(EnvironmentSetup):
    def test_01(self):
        driver = self.driver
        objCommonUtils = CommonUtils(driver)
        print ('Hello World')
        #print(objCommonUtils.prjPath())