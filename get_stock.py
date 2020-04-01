pip install xlrd 

import requests
import urllib.parse
import os
import xlrd

location = ("M:\Programming\Python\Python Stock Market Project\Ticker Symbols.xlsx")
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
sheet.cell value(0,0)

for tickers in range(sheet.nrows):
    tickers = (sheet.cell_value(i,0))

def get_stock(symbol):
    safe_symbol = urllib.parse.quote(symbol, safe='')
    r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/{}?period1=475804800&period2=1585094400&interval=1d&events=history'.format(safe_symbol), allow_redirects=True)
    print('downloading data for ' + symbol)
    os.makedirs(os.path.dirname('/data/{}.csv'.format(symbol)), exist_ok=True)
    open('./data/{}.csv'.format(symbol), 'wb').write(r.content)


stocks = tickers
for stock in stocks:
    get_stock(stock)
