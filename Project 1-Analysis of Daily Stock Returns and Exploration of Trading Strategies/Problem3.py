"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. the best and worst days of the week for each
"""

import pandas as pd
print("\n ********************     Question 3.1  ******************* ")

# Read the data from CSV files
zg = pd.read_csv('ZG.csv', parse_dates=['Date'], index_col='Date')
spy = pd.read_csv('SPY.csv', parse_dates=['Date'], index_col='Date')

# Combine the data into a single dataframe
df = pd.concat({'ZG': zg['Adj Close'], 'SPY': spy['Adj Close']}, axis=1)

# Resample the data to get the daily close prices
df = df.resample('D').last()

# Calculate the aggregate table for each stock
print("Close:last trading day close price.       Volume:per week sum ")
zg_agg = zg.resample('W').agg({'Adj Close': 'last', 'Volume': 'sum'})
spy_agg = spy.resample('W').agg({'Adj Close': 'last', 'Volume': 'sum'})

print("Aggregate table for ZG:\n", zg_agg)
print("Aggregate table for SPY:\n", spy_agg)
# Calculate the mean daily return for each day of the week
zg_mean_returns = df['ZG'].groupby(df.index.weekday).mean()
spy_mean_returns = df['SPY'].groupby(df.index.weekday).mean()


# Print the results
print("0:Monday  1:Tuesday  2:Wednesday  3:Thursday  4:Friday  5:Saturday  6:Sunday")
print("ZG mean returns by weekday:\n", zg_mean_returns)
print("SPY mean returns by weekday:\n", spy_mean_returns)


# Rank the days based on their returns
zg_best_day = zg_mean_returns.idxmax()
zg_worst_day = zg_mean_returns.idxmin()
spy_best_day = spy_mean_returns.idxmax()
spy_worst_day = spy_mean_returns.idxmin()

print("Best day of the week for ZG: ", zg_best_day)
print("Worst day of the week for ZG: ", zg_worst_day)
print("Best day of the week for SPY: ", spy_best_day)
print("Worst day of the week for SPY: ", spy_worst_day)

print("\n ********************     Question 3.2  ******************* ")
print("0:Monday  1:Tuesday  2:Wednesday  3:Thursday  4:Friday  5:Saturday  6:Sunday")
if zg_best_day == spy_best_day:
    print("The best day of the week is the same for ZG and SPY: ", zg_best_day)
else:
    print("The best day of the week is different for ZG and SPY.")
    print("For ZG, the best day is: ", zg_best_day)
    print("For SPY, the best day is: ", spy_best_day)

if zg_worst_day == spy_worst_day:
    print("The worst day of the week is the same for ZG and SPY: ", zg_worst_day)
else:
    print("The worst day of the week is different for ZG and SPY.")
    print("For ZG, the worst day is: ", zg_worst_day)
    print("For SPY, the worst day is: ", spy_worst_day)

