import os
import xlrd
import csv

def get_company_names():
    #opens Excel File
    location = ("./Ticker Symbols.xlsx")
    workbook = xlrd.open_workbook(location)
    sheet = workbook.sheet_by_index(0)

    #Makes List From Excel Column
    stocks = {}
    for row in range(1,sheet.nrows):
        stocks[str(sheet.cell_value(row,0))] = sheet.cell_value(row,1)
    return stocks
