import requests
import urllib.parse
import os
import xlrd
from tqdm import tqdm

#Opens Excel File
location = ("./Ticker Symbols.xlsx")
workbook = xlrd.open_workbook(location)
sheet = workbook.sheet_by_index(0)

#Makes List From Excel Column
tickers = []
for ticker_symbols in range(sheet.nrows):
    tickers.append(sheet.cell_value(ticker_symbols,0))
tickers.pop(0)

#Scrapes web for data, makes .csv files for each ticker
def get_stock(symbol):
    safe_symbol = urllib.parse.quote(symbol, safe='')
    r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/{}?period1=475804800&period2=1585094400&interval=1d&events=history'.format(safe_symbol), allow_redirects=True)
    # print('downloading data for ' + symbol)
    os.makedirs(os.path.dirname('/data/{}.csv'.format(symbol)), exist_ok=True)
    open('./data/{}.csv'.format(symbol), 'wb').write(r.content)

#Takes each ticker symbol, and downloads the data for it
for stock in tqdm(tickers):
    get_stock(stock)
