
"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. each of the scenarios a,b and c, compute the final amount
2. computer gain by missing the worst days or by missing the best days
"""
import pandas as pd
print("\n ********************     Question 6.1   ******************* ")
ZG = pd.read_csv('ZG.csv')
SPY = pd.read_csv('SPY.csv')
# Set initial amount of ZG
initial_amount_ZG_1 = 100
largest_10returns_ZG = list(ZG['Return'].nlargest(10))
# The return is evaluated when it is greater than 0 and not the biggest 10
for index, row in ZG.iterrows():
    return_value_ZG = row['Return']
    if return_value_ZG > 0 and return_value_ZG not in largest_10returns_ZG:
        # Calculate final amount for current trading day
        final_amount_ZG_lostBest = initial_amount_ZG_1 * (1 + return_value_ZG)
        # Update initial amount for next trading day
        initial_amount_ZG_1 = final_amount_ZG_lostBest


# Set initial amount of SPY
initial_amount_SPY_1 = 100
largest_10returns_SPY = list(SPY['Return'].nlargest(10))
# The return is evaluated when it is greater than 0 and not the biggest 10
for index, row in SPY.iterrows():
    return_value_SPY = row['Return']
    if return_value_SPY > 0 and return_value_SPY not in largest_10returns_SPY:
        # Calculate final amount for current trading day
        final_amount_SPY_lostBest = initial_amount_SPY_1 * (1 + return_value_SPY)
        # Update initial amount for next trading day
        initial_amount_SPY_1 = final_amount_SPY_lostBest

# Print final amount

print("scenario(a):")
print("Final amount of ZG with wrong results for the best 10 trading days: ${:.2f}".format(final_amount_ZG_lostBest))
print("Final amount of SPY with wrong results for the best 10 trading days: ${:.2f}".format(final_amount_SPY_lostBest))


# Set initial amount of ZG
initial_amount_ZG_2 = 100
lowest_10returns_ZG = list(ZG['Return'].nsmallest(10))
# The return is evaluated when it is greater than 0 or is the lowest 10
for index, row in ZG.iterrows():
    return_value_ZG = row['Return']
    if return_value_ZG > 0 or return_value_ZG in lowest_10returns_ZG:
        # Calculate final amount for current trading day
        final_amount_ZG_lostWorst = initial_amount_ZG_2 * (1 + return_value_ZG)
        # Update initial amount for next trading day
        initial_amount_ZG_2 = final_amount_ZG_lostWorst

# Set initial amount of SPY
initial_amount_SPY_2 = 100
lowest_10returns_SPY = list(SPY['Return'].nsmallest(10))
# The return is evaluated when it is greater than 0 or is the lowest 10
for index, row in SPY.iterrows():
    return_value_SPY = row['Return']
    if return_value_SPY > 0 or return_value_SPY in lowest_10returns_SPY:
        # Calculate final amount for current trading day
        final_amount_SPY_lostWorst = initial_amount_SPY_2 * (1 + return_value_SPY)
        # Update initial amount for next trading day
        initial_amount_SPY_2 = final_amount_SPY_lostWorst

# Print final amount
print("\nscenario(b):")
print("Final amount of ZG with wrong results for the worst 10 trading days: ${:.2f}".format(final_amount_ZG_lostWorst))
print("Final amount of SPY with wrong results for the worst 10 trading days: ${:.2f}".format(final_amount_SPY_lostWorst))


# Set initial amount of ZG
initial_amount_ZG_3 = 100
biggest_5returns_ZG = list(ZG['Return'].nlargest(5))
lowest_5returns_ZG = list(ZG['Return'].nsmallest(5))
# The return is evaluated when it is greater than 0 and not the biggest 5 or is the lowest 5
for index, row in ZG.iterrows():
    return_value_ZG = row['Return']
    if (return_value_ZG > 0 and return_value_ZG not in biggest_5returns_ZG) \
            or return_value_ZG in lowest_5returns_ZG:
        # Calculate final amount for current trading day
        final_amount_ZG_BestWorst = initial_amount_ZG_3 * (1 + return_value_ZG)
        # Update initial amount for next trading day
        initial_amount_ZG_3 = final_amount_ZG_BestWorst


# Set initial amount of SPY
initial_amount_SPY_3 = 100
biggest_5returns_SPY = list(SPY['Return'].nlargest(5))
lowest_5returns_SPY = list(SPY['Return'].nsmallest(5))
# The return is evaluated when it is greater than 0 and not the biggest 5 or is the lowest 5
for index, row in SPY.iterrows():
    return_value_SPY = row['Return']
    if (return_value_SPY > 0 and return_value_SPY not in biggest_5returns_SPY) \
            or return_value_SPY in lowest_5returns_SPY:
        # Calculate final amount for current trading day
        final_amount_SPY_BestWorst = initial_amount_SPY_3 * (1 + return_value_SPY)
        # Update initial amount for next trading day
        initial_amount_SPY_3 = final_amount_SPY_BestWorst

# Print final amount
print("\nscenario(c):")
print("Final amount of ZG with the wrong best and worst 5 trading days: ${:.2f}".format(final_amount_ZG_BestWorst))
print("Final amount of SPY with the wrong best and worst 5 trading days:${:.2f}".format(final_amount_SPY_BestWorst))


print("\n ********************     Question 6.2   ******************* ")
if final_amount_ZG_lostBest > final_amount_ZG_lostWorst:
    print(" For ZG: missing the 10 best days gain more than missing the 10 worst days")
else:
    if final_amount_ZG_lostBest == final_amount_ZG_lostWorst:
        print("For ZG:They are same")
    else:
        final_amount_ZG_lostBest < final_amount_ZG_lostWorst
    print(" For ZG:missing the 10 worst days gain more than missing the 10 best days")

if final_amount_SPY_lostBest > final_amount_SPY_lostWorst:
    print(" For SPY: missing the 10 best days gain more than missing the 10 worst days")
else:
    if final_amount_SPY_lostBest == final_amount_SPY_lostWorst:
        print("For SPY:They are same")
    else:
        final_amount_SPY_lostBest < final_amount_SPY_lostWorst
        print(" For SPY:missing the 10 worst days gain more than missing the 10 best days")

print("\n ********************     Question 6.2   ******************* ")
question4_ZG_money=155080075.22
question4_SPY_money=11985.02
if question4_ZG_money > final_amount_ZG_BestWorst:
    print(" For ZG: the gain in question 4 is higher,gain more: ${:.2f}".format(question4_ZG_money - final_amount_ZG_BestWorst))
else:
    if question4_ZG_money == final_amount_ZG_BestWorst:
        print("For ZG:They are same")
    else:
        question4_ZG_money < final_amount_ZG_BestWorst
    print(" For ZG: the gain in question 6 is higher,gain more: ${:.2f}".format(final_amount_ZG_BestWorst - question4_ZG_money))

if question4_SPY_money > final_amount_SPY_BestWorst:
    print(" For SPY: the gain in question 4 is higher,gain more: ${:.2f}".format(question4_SPY_money - final_amount_SPY_BestWorst))
else:
    if question4_SPY_money == final_amount_SPY_BestWorst:
        print("For SPY:They are same")
    else:
        question4_SPY_money < final_amount_SPY_BestWorst
        print(" For SPY: the gain in question 6 is higher,gain more: ${:.2f}".format(final_amount_SPY_BestWorst - question4_SPY_money))