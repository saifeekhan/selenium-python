import os
# dirpath = os.getcwd()
# print("Current working directory: "+dirpath)
# foldername= os.path.basename(dirpath)
# print ("Direcoty name is:" + foldername)

####################3
absFilePath = os.path.abspath(__file__)
print (absFilePath)
fileDir = os.path.dirname(absFilePath)
print (fileDir)
dir=os.path.dirname(fileDir)
print (dir)