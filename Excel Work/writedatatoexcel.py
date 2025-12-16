import openpyxl

wk= openpyxl.Workbook()
sh = wk.active
print(sh.title)
sh.title="HelloTestingWorlds"

print(sh.title)
sh['A4'].value="www.testingworld.com "

#@nd sheet is created below
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A3']="8736893768934"

#Remove Sheet
wk.remove(wk['HelloTestingWorlds'])
#Saving
wk.save("D:\\pysheet.xlsx")