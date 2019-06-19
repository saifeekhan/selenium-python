'''
Created on Jun 19, 2019

@author: saif.khan
'''
import os
class CommonUtils():
    # Function to return the path of the project directory
    def prjPath(self):
        prjName = "Selenium-Python"
        self.prjDir=os.path.abspath(__file__)
        while (self.prjDir[-15:]!=prjName):
            self.prjDir = os.path.dirname(self.prjDir)
        
        return self.prjDir
