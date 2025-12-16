import openpyxl

wk= openpyxl.Workbook()
sh = wk.active
print(sh.title)
sh.title="HelloTestingWorlds"