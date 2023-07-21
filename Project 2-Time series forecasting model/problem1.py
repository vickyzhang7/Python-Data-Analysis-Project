"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/29/2023
Homework 2 problem 1
Description of problem:
1. give ”True Label”
2.computer probability p∗
3.seeing k consecutive ”down days”, the next day is an ”up day” Compute this for k = 1, 2, 3.
4.seeing k consecutive ”up days”, the next day is still an ”up day” Compute this for k = 1, 2, 3.
"""
import pandas as pd
print("\n ********************     Question 1.1    ******************* ")
my_stock = pd.read_csv('ZG.csv')
SPY = pd.read_csv('SPY.csv')

def add_column(file_name):
    True_label = []
    for row in file_name['Return']:
        if row < 0:
            True_label.append('-')
        else:
            True_label.append('+')
    file_name['True_label'] = True_label
    print(file_name)

add_column(my_stock)
add_column(SPY)

print("\n ********************     Question 1.2    ******************* ")
ZG_training = my_stock[(my_stock['Year'] >= 2018) & (my_stock['Year'] <= 2020)]
SPY_training = SPY[(SPY['Year'] >= 2018) & (SPY['Year'] <= 2020)]

# the ratio of ZG 'UP' Stocks
ratio1 = len(ZG_training.loc[ZG_training.True_label == '+']) / (len(ZG_training.loc[ZG_training.True_label == '+'])+len(ZG_training.loc[ZG_training.True_label == '-']))
# the ratio of SPY 'UP' Stocks
ratio2 = len(SPY_training.loc[SPY_training.True_label == '+']) / (len(SPY_training.loc[SPY_training.True_label == '+'])+len(SPY_training.loc[SPY_training.True_label == '-']))

print(f'For ZG stock, the default probability that the next day is a "up" day is {ratio1:.4f}.'
      f'\nFor SPY stock, the default probability that the next day is a "up" day is {ratio2:.4f}.')

print("\n ********************     Question 1.3    ******************* ")
# seeing k consecutive ”down days”, the next day is an ”up day”
def detect_match(list_converted_to_string, pattern, opposed_pattern):
    pattern_count = list_converted_to_string.count(pattern)
    opposed_pattern_count = list_converted_to_string.count(opposed_pattern)
    return pattern_count / (pattern_count + opposed_pattern_count)

# Convert the True_label column into a string
ZG_True_Label_list = ZG_training['True_label'].to_list()
ZG_str = ''.join(str(x) for x in ZG_True_Label_list)

SPY_True_Label_list = SPY_training['True_label'].to_list()
SPY_str = ''.join(str(x) for x in SPY_True_Label_list)

print(f'For ZG, when K=1, the probability that after seeing k consecutive ”down days" the next day is an ”up day” is {detect_match(ZG_str, "-+", "--"):.4f}.'
      f'\nFor ZG, when K=2, the probability that after seeing k consecutive ”down days" the next day is an ”up day” is {detect_match(ZG_str, "--+", "---"):.4f}.'
      f'\nFor ZG, when K=3, the probability that after seeing k consecutive ”down days” the next day is an ”up day” is {detect_match(ZG_str, "---+", "----"):.4f}.'
      f'\nFor SPY, when K=1, the probability that after seeing k consecutive ”down days” the next day is an ”up day” is {detect_match(SPY_str, "-+", "--"):.4f}.'
      f'\nFor SPY, when K=2, the probability that after seeing k consecutive ”down days” the next day is an ”up day” is {detect_match(SPY_str, "--+", "---"):.4f}.'
      f'\nFor SPY, when K=3, the probability that after seeing k consecutive ”down days” the next day is an ”up day” is {detect_match(SPY_str, "---+", "----"):.4f}.')

print("\n ********************     Question 1.4    ******************* ")

print(f'For ZG, when K=1, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(ZG_str, "++", "+-"):.4f}.'
      f'\nFor ZG, when K=2, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(ZG_str, "+++", "++-"):.4f}.'
      f'\nFor ZG, when K=3, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(ZG_str, "++++", "+++-"):.4f}.'
      f'\nFor SPY, when K=1, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(SPY_str, "++", "+-"):.4f}.'
      f'\nFor SPY, when K=2, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(SPY_str, "+++", "++-"):.4f}.'
      f'\nFor SPY, when K=3, the probability that after seeing k consecutive ”up days” the next day is an ”up day” is {detect_match(SPY_str, "++++", "+++-"):.4f}.')

