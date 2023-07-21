
"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. ”buy-and-hold” strategy:money will you have on the last trading day of 2020
2.compare with results obtained in question 4
"""
import pandas as pd
print("\n ********************     Question 5.1   ******************* ")

# Load the ZG and SPY data
zg_data = pd.read_csv("ZG.csv", index_col="Date", parse_dates=True)
spy_data = pd.read_csv("SPY.csv", index_col="Date", parse_dates=True)

# Calculate the daily returns for each stock
# The result of use Adj.Close or Return are same
zg_returns = zg_data["Adj Close"][-1] / zg_data["Adj Close"][0] - 1
spy_returns = spy_data["Adj Close"][-1] / spy_data["Adj Close"][0] - 1

# Calculate the final amount of money for each stock
ZG_final_amount = 100 * (1 + zg_returns)
SPY_final_amount = 100 * (1 + spy_returns)

print("Final amount for ZG stock (buy-and-hold): ${:.2f}".format(ZG_final_amount))
print("Final amount for SPY stock (buy-and-hold): ${:.2f}".format(SPY_final_amount))


print("\n ********************     Question 5.2  ******************* ")

question4_ZG_money=155080075.22
question4_SPY_money=11985.02
print("Final amount of money in question 4 for the ZG only strategy: ${:.2f}". format(question4_ZG_money))
print("Final amount of money in question 4 for the SPY only strategy: ${:.2f}". format(question4_SPY_money))
if(question4_ZG_money > ZG_final_amount):
    print("The question 4 for ZG get higher profit: ${:.2f}".format(question4_ZG_money - ZG_final_amount))
else:
    print("The question 4 for ZG get lose: ${:.2f}".format(ZG_final_amount - question4_ZG_money))

if(question4_SPY_money>SPY_final_amount):
    print("The question 4 for SPY get higher profit: ${:.2f}".format(question4_SPY_money - SPY_final_amount))
else:
    print("The question 4 for SPY get lose: ${:.2f}".format(SPY_final_amount - question4_SPY_money))



