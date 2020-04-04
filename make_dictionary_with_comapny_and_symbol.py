import xlrd

def get_company_names():
    #opens Excel File
    location = ("./Ticker Symbols.xlsx")
    workbook = xlrd.open_workbook(location)
    sheet = workbook.sheet_by_index(0)

    #Makes Dictionary From Excel Column
    company_and_ticker_symbol_dictionary = {}
    for row in range(1,sheet.nrows):
        company_and_ticker_symbol_dictionary[str(sheet.cell_value(row,0))] = sheet.cell_value(row,1)
    return company_and_ticker_symbol_dictionary


