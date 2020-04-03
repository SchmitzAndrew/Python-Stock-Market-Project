import os
import xlrd
import csv

#opens Excel File
location = ("./Ticker Symbols.xlsx")
workbook = xlrd.open_workbook(location)
sheet = workbook.sheet_by_index(0)

#Makes List From Excel Column
company_names = []
for company_name in range(sheet.nrows):
    company_names.append(sheet.cell_value(company_name,1))
company_names.pop(0)

print (company_names)



