
"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1 Preliminary for problem 3
Description of problem:
1.to read your saved ZG.CSV file into a list of lines
"""
import os

ticker = 'ZG'
input_dir = r'/Users/mac/Desktop/weiqi_hw_1'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)












