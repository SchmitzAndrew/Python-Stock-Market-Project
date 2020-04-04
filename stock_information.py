import time, webbrowser

#Pulls modules from other sections of code
from stock_analysis import get_avg, get_max, get_min
from make_dictionary_with_comapny_and_symbol import get_company_names
company_and_ticker_symbol_dictionary = get_company_names()

#I or F -> Makes decision on starting choice
def information_or_lookup():
    starting_decision = input("I for info, F for lookup")
    if starting_decision.lower() == "i":
        ticker_information()
    elif starting_decision.lower() == "f":
        csv_file_opener()


#I -> Information on ticker symbols
def ticker_information():
    information_selection = input("F to Find the ticker symbol based on the company name, C for Common ticker symbols, E to Explain ticker symbols")
    if information_selection.lower() == "f":
        ticker_symbol_from_company_name()
    elif information_selection.lower() == "c":
        common_ticker_symbols()
    elif information_selection.lower() == "e":
        explain_ticker_symbols()
    else:
        print("Not a valid entry")
        ticker_information()

#F -> Finds the Ticker Symbol after the user enters a company name. Uses the file produced by make_dictionary_with_company_and_symbol.py.
def ticker_symbol_from_company_name():
    print("This tool can find the ticker symbol based off a company name.")
    company_name_to_find_symbol_for = input("Enter the complete name of the company as listed on the NYSE.")
    results = [company for company in company_and_ticker_symbol_dictionary if company_name_to_find_symbol_for in company_and_ticker_symbol_dictionary[company]]
    for result in results:
        print(result + "->" + company_and_ticker_symbol_dictionary [result])
    information_or_lookup()

#C -> Displays common ticker symbols and directs to webpage with common ones from all exchanges.
def common_ticker_symbols():
    print('''Common ticker symbols include 
          Berkshire Hathaway: BRK.A
          Alibaba Group: BABA
          Johnson & Johnson: JNJ
          JPMorgan Chase & Co.: JPM
          Exxon Mobil: XOM
          Walmart: WMT''')
    time.sleep(1)
    print('''These are the largest companies that are listed on the New York Stock Exchange. 
          Other major companies, such as Apple, Google, or Microsoft, are listed on the National Association of Securities Dealers Automated Quotations or NASDAQ.
          To see the top 30 companies based on Market Cap, regardless of exchange, press MC.
          Insert anything else to return to start.''')
    link_to_top_30_companies = input("Enter MC to see list")
    if link_to_top_30_companies.lower() == "mc":
        webbrowser.open("https://www.fool.com/investing/2017/12/05/the-30-largest-companies-on-the-stock-market.aspx")
        information_or_lookup()
    else:
        print("Redirecting to start")
        information_or_lookup()

#E -> Gives information on ticker symbols and shares webpage with more info
def explain_ticker_symbols():
    print("Ticker Symbols represent all of the stocks within exchanges, which is the NYSE in this case.")
    print("Each company has a unique representation, and some have special features that differentiate them. ")
    print("An example of this is mutual funds, which have an X at the end of their ticker symbol.")
    print("Would you like to view more information on ticker symbols?")
    more_info_on_ticker_symbols = input("Enter MI to revieve more infomation.")
    if more_info_on_ticker_symbols.lower() == "mi":
        webbrowser.open("https://www.investopedia.com/terms/t/tickersymbol.asp")
        information_or_lookup()
    else:
        information_or_lookup()

#Finds The .csv File Based on the Ticker Symbol entered so it can be read/ sent to stock_analysis
def csv_file_opener():
    print(" Search for a Ticker Symbol based on a company's name.")
    ticker_symbol_entry = input("Enter the complete ticker symbol for the company you want data for. Do not enter NYSE-, just the symbol.")
    if ticker_symbol_entry.upper() in company_and_ticker_symbol_dictionary:
        filename_for_finding_stock = ("./data/" + ticker_symbol_entry +".csv")
        with open (filename_for_finding_stock, 'r') as csvfile:
            stock_analysis(csvfile)
    else:
        print('''Stock is not in our database.
              Common Errors:
              1)Stock is listed in NASDAQ, not NYSE
              2)The full ticker symbol with no errors. 
              Use the services provided in information to find ticker symbols''')
        information_or_lookup()


#links to stock_analysis.py
def stock_analysis(information_from_csvs):
    print(" Use numbers to select what operation you would like to use. The operations are Max, Min, Avg. The data is pulled from the adjusted closing value each day.")
    operation_selection = input("MAX,MIN,AVG")
    if operation_selection.lower() == "max":
        print (get_max(information_from_csvs))
        information_or_lookup()
    elif operation_selection.lower() == "min":
        print (get_min(information_from_csvs))
        information_or_lookup()
    elif operation_selection.lower() == "avg":
        print (get_avg(information_from_csvs))
        information_or_lookup()
    else:
        information_or_lookup()

#Starter Instructions
print("This tool can be used to find financial data for all of the stocks listed within the NYSE and provide information about companies and their ticker symbols.")
time.sleep(.4)
print("To find information about Ticker Symbols, press I. To find information about a certain stock that you know the Ticker Symbol for, press F.")

information_or_lookup()


