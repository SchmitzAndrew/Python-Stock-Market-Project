import os
import time
import webbrowser

#instructions
print("This tool can be used to find financial data for all of the stocks listed within the NYSE and provide information about companies and their ticker symbols.")
time.sleep(.4)
print("To find information about Ticker Symbols, press I. To find information about a certain stock that you know the Ticker Symbol for, press F.")

#I or S -> Makes decision on starting choice
def information_or_lookup():
    starting_decision = input("I for info, F for lookup")
        if starting_decision == "I"
            ticker_information()
        elif starting_decision == "F"
            ticker_symbol_finder()


#I -> Information on ticker symbols
def ticker_information():
    information_selection = input("F to Find the ticker symbol based on the company name, C for Common ticker symbols, E to Explain ticker symbols")
        if information_selection == "F":
            ticker_symbol_finder()
        if information_selection == "C":
            common_ticker_symbols()
        if information_selection == "E":
            explain_ticker_symbols()
        elif
            #Does something need to be where the elif is?
            print(" Not a valid entry")
            ticker_infromation()

#F -> Finds the Ticker Symbol after the user enters a company name. Uses the file produced by company_names_from_excel_to_csv_file.py.
def ticker_symbol_from_company_name():
    print("This tool can find the ticker symbol based off a company name.")
    company_name_to_find_symbol_for = input("Enter the complete name of the company as listed on the NYSE.")

#C
def common_ticker_symbols():
    print("Common ticker symbols include "
          "Berkshire Hathaway: BRK.A"
          "Alibaba Group: BABA"
          "Johnson & Johnson: JNJ"
          "JPMorgan Chase & Co.: JPM"
          "Exxon Mobil: XOM"
          "Walmart: WMT")
    print("These are the largest companies that are listed on the New York Stock Exchange. Other major companies, such as Apple, Google, or Microsoft, are listed on the National Association of Securities Dealers Automated Quotations.")
    print("To see the top 30 companies based on Market Cap, regardless of exchange, press MC")
    link_to_top_30_companies = input("Enter MC to see list")
        if link_to_top_30_companies == "MC"
            webbrowser.open(https://www.fool.com/investing/2017/12/05/the-30-largest-companies-on-the-stock-market.aspx)
        elif
            print("Redirecting to start")
            information_or_lookup()

#E
def explain_ticker_symbols():
    print("Ticker Symbols represent all of the stocks within exchanges, which is the NYSE in this case.")
    time.sleep(.5)
    print("Each company has a unique representation, and some have special features that differentiate them. ")
    time.sleep(.5)
    print("An example of this is mutual funds, which have an X at the end of their ticker symbol.")
    time.sleep(.5)
    print("Would you like to view more information on ticker symbols?")
    more_info_on_ticker_symbols = input("Enter MI to revieve more infomation.")
        if more_info_on_ticker_symbols == "MI":
            webbrowser.open(https://www.investopedia.com/terms/t/tickersymbol.asp)
        elif
            ticker_information()


# Finds The .csv File Based on the Ticker Symbol entered so it can be read/ sent to stock_analysis
def .csv file opener():
    print(" Search for a Ticker Symbol based on a company's name.")
        ticker_symbol_entry = input("Enter the complete ticker symbol for the company you want data for. Do not enter NYSE-, just the symbol.")
    filename_for_finding_stock = (ticker_symbol_entry +.csv)
    with open ('filename_for_finding_stock', 'rb') as csvfile:
#what else needs to be added here?
    stock_analysis()

#max, minimum, mean price
def stock_analysis():








