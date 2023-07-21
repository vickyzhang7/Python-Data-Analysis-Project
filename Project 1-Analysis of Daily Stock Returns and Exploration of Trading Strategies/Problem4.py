"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. the money will you have on the last trading day
"""
import pandas as pd
print("\n ********************     Question 4.1 and 4,2  ******************* ")
# Set initial amount of ZG
# Read SPY data
ZG = pd.read_csv('ZG.csv')
SPY = pd.read_csv('SPY.csv')
initial_amount_ZG = 100
initial_amount_SPY = 100

# The return is evaluated only if it is greater than 0, and the return less than 0 is not evaluated
for index, row in ZG.iterrows():
    return_value_ZG = row['Return']
    if return_value_ZG > 0:
        # Calculate final amount for the current trading day
        final_amount_ZG = initial_amount_ZG * (1 + return_value_ZG)
        # Update initial amount for the next trading day,to get a new one
        initial_amount_ZG = final_amount_ZG

# The return is evaluated only if it is greater than 0, and the return less than 0 is not evaluated
for index, row in SPY.iterrows():
    return_value_SPY = row['Return']
    if return_value_SPY > 0:
        # Calculate final amount for current trading day
        final_amount_SPY = initial_amount_SPY * (1 + return_value_SPY)
        # Update initial amount for next trading day
        initial_amount_SPY = final_amount_SPY

# Print final amount
print("Final amount of money for the ZG only strategy: ${:.2f}". format(final_amount_ZG))
print("Final amount of money for the SPY only strategy: ${:.2f}". format(final_amount_SPY))




