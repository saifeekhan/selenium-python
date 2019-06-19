import sys
import openpyxl
from test.utils.CommonUtils import CommonUtils

class ExcelDataProvider:
    cUtils : CommonUtils
    
    def __init__(self):
        self.cUtils = CommonUtils()
        self.path = self.cUtils.prjPath() + "/testData/MarlinTestData.xlsx"
        try:
            self.workbook = openpyxl.load_workbook(self.path)
        except:
            print ("Unable to load file.")
            sys.exit()


    def getStringData(self, sheet, row, col):
        self.sheet = self.workbook.active
        return self.sheet.cell(row=row, column=col).value
