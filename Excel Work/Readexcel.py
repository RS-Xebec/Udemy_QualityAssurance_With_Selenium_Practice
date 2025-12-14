#Import Package
import openpyxl

#Load Workbook

wk = openpyxl.load_workbook("D:\\UDEMY\\TestData.xlsx")

print(wk.sheetnames)
print("Active sheet is: " + wk.active.title)

#Create object of any sheet you want to work

sh = wk['Sheet1']
print(sh.title)
