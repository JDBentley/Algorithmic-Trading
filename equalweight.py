# import dependencies
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

# import API token
from secrets import IEX_CLOUD_API_TOKEN

# import our stock list
stocks = pd.read_csv('sp_500_stocks.csv')

# making our first API call
symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
print(data)

# parsing API call
data ['latestPrice']
data ['marketCap']

# adding stocks to data frames
my_columns = ['Ticker', 'Price', 'Market Capitalization', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
print(final_dataframe)

final_dataframe = final_dataframe.append(
    pd.Series([
        'AAPL', 
        data['latestPrice'], 
        data['marketCap'], 
        'N/A'], 
        index = my_columns
    ),
    ignore_index = True
)
print(final_dataframe)

#looping through the tickers in our list of stocks
final_dataframe = pd.DataFrame(columns = my_columns)
for symbol in stocks['Ticker']:
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
        pd.Series(
            [symbol,
            data['latestPrice'],
            data['marketCap'],
            'N/A'],
            index = my_columns
        ),
        ignore_index= True
    )
print(final_dataframe)

