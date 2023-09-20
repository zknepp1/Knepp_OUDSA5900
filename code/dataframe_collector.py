import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re
import yfinance as yf


# This class will be used to retrieve the financial data, and news data
class DataFrameCollection:
    def __init__(self, tickers, startdate, enddate):
        self.list_of_tickers = tickers
        self.dataframes = []
        self.start_date = startdate
        self.end_date = enddate
        #self.end_date = datetime.now().strftime('%Y-%m-%d')

    # Computes average rolling windows for a dataframe. Returns dataframe with new columns
    def make_rolling_window(self, dataframe, window_size, size):
        numbers_series = dataframe['Close']
        windows = numbers_series.rolling(window_size)
        moving_averages = windows.mean()
        moving_averages_list = moving_averages.tolist()
        column_name = str(size) + '_day_rolling'
        dataframe[column_name] = moving_averages_list
        return dataframe

    # Uses yfinance to go retrieve ticker data
    def retrieve_financial_data(self):
        for i in self.list_of_tickers:
            data = yf.Ticker(i)
            hist = data.history(start=self.start_date, end=self.end_date)
            dataframe = pd.DataFrame(hist)

            dataframe['date'] = dataframe.index
            pattern = r'\d\d\d\d-\d\d-\d\d'
            re_matches = []

            for value in dataframe['date']:
                value = str(value)
                match = re.search(pattern, value)
                if match:
                    re_matches.append(match.group())
                else:
                    re_matches.append('no match')

            dataframe['dt'] = re_matches
            dataframe['dt'] = pd.to_datetime(dataframe['dt'], format='%Y-%m-%d')
            dataframe.set_index('dt', inplace=True)


            window_size = 5
            window_size2 = 10
            window_size3 = 20
            dataframe = self.make_rolling_window(dataframe, window_size, 'five')
            dataframe = self.make_rolling_window(dataframe, window_size2, 'ten')
            dataframe = self.make_rolling_window(dataframe, window_size2, 'twenty')

            # Right here I am determining What i am trying to predict
            # This is the closing price for the stock 20 days ahead of time
            dataframe['stock'] = i
            dataframe['Target'] = dataframe['Close'].shift(-20)
            dataframe.dropna(inplace=True)

            self.dataframes .append(dataframe)


    # This function retrieves the local news dataset
    def save_data(self):
        path = '/home/zacharyknepp2012/Knepp_OUDSA5900/fdata/'
        for idx, df in enumerate(self.dataframes):
          file_name  =  f"df_{idx}.csv"
          df.to_csv(path + file_name, index = False)


    # Returns the financial data for all tickers specified. Returns a list item
    def return_dataframes(self):
        return self.dataframes
