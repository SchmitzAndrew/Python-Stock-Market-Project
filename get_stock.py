import requests
import urllib.parse
import os
import xlrd
from tqdm import tqdm

location = ("./Ticker Symbols.xlsx")
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

tickers = []
for i in range(sheet.nrows):
    tickers.append(sheet.cell_value(i,0))
tickers.pop(0)


def get_stock(symbol):
    safe_symbol = urllib.parse.quote(symbol, safe='')
    r = requests.get('https://query1.finance.yahoo.com/v7/finance/download/{}?period1=475804800&period2=1585094400&interval=1d&events=history'.format(safe_symbol), allow_redirects=True)
    # print('downloading data for ' + symbol)
    os.makedirs(os.path.dirname('/data/{}.csv'.format(symbol)), exist_ok=True)
    open('./data/{}.csv'.format(symbol), 'wb').write(r.content)


for stock in tqdm(tickers):
    get_stock(stock)
