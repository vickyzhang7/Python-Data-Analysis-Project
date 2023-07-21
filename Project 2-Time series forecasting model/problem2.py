import pandas as pd
#add true label in problem1
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

ZG_training = my_stock[(my_stock['Year'] >= 2018) & (my_stock['Year'] <= 2020)]
SPY_training = SPY[(SPY['Year'] >= 2018) & (SPY['Year'] <= 2020)]
# Convert the True_label column into a string
ZG_True_Label_list = ZG_training['True_label'].to_list()
ZG_str = ''.join(str(x) for x in ZG_True_Label_list)
SPY_True_Label_list = SPY_training['True_label'].to_list()
SPY_str = ''.join(str(x) for x in SPY_True_Label_list)

print("\n ********************     Question 2.1    ******************* ")
# get all patterns:"s"
x=['--', '-+', '+-', '++']
y=['---', '--+', '-+-', '-++', '+--', '+-+', '++-', '+++']
z=['----', '---+', '--+-', '--++', '-+--', '-+-+', '-++-', '-+++', '+---', '+--+', '+-+-', '+-++', '++--', '++-+', '+++-', '++++']

# predict the next day label
def predicted_label(list, patterns):
    pattern_list = []
    results_list = []
    #to caculate the number of the number N− and the number of N+
    for s in patterns:
        pattern_list.append(s)
        if list.count(s + "-") > list.count(s + "+"):
            results_list.append("-")
        elif list.count(s + "-") < list.count(s + "+"):
            results_list.append("+")
        else:
            results_list.append("+")
    predicted_label = dict(zip(pattern_list, results_list))
    return predicted_label

# the predicted labels of ZG stocks with W =2,3,4.
ZG_2 = predicted_label(ZG_str, x)
ZG_3 = predicted_label(ZG_str, y)
ZG_4 = predicted_label(ZG_str, z)

# the predicted labels of SPY stocks with W =2,3,4.
SPY_2 = predicted_label(SPY_str, x)
SPY_3 = predicted_label(SPY_str, y)
SPY_4 = predicted_label(SPY_str, z)


# print all the outcomes
def output(dictionary):
    for key, value in dictionary.items():
        print(f'the predicted label of the patterns {key} is {value}')


# print all rules of the predicted label of ZIONL STOCKS when W=2,3,4
print("For ZG STOCKS:\nWhen W=2:")
output(ZG_2)
print('When W=3:')
output(ZG_3)
print('When W=4:')
output(ZG_4)

# print all rules of the predicted label of SPY STOCKS when W=2,3,4
print("For SPY STOCKS:\nWhen W=2:")
output(SPY_2)
print('When W=3:')
output(SPY_3)
print('When W=4:')
output(SPY_4)

# Add predict label columns into testing dataset
# Split the test dataset from the original dataset
ZG_testing = my_stock[(my_stock['Year'] >= 2020) & (my_stock['Year'] <= 2021)]
SPY_testing = SPY[(SPY['Year'] >= 2020) & (SPY['Year'] <= 2021)]

#  Convert the True label column in to a string
ZG_True_Label_list_testing = ZG_testing['True_label'].to_list()
ZG_str_testing = ''.join(str(x) for x in ZG_True_Label_list_testing)

SPY_True_Label_list_testing = SPY_testing['True_label'].to_list()
SPY_str_testing = ''.join(str(x) for x in SPY_True_Label_list_testing)


# According to w=2,3 and 4, to create the new predict label
def new_predict_label(testing_str, patterns_dic, w):
    predicted_label = testing_str[0:w]
    for i in range(len(testing_str) - w):
        a = testing_str[i:i + w]
        predicted_label += patterns_dic[a]
    return predicted_label


# Get all new predict label with W=2,3 and 4
ZG_2_predict = new_predict_label(ZG_str_testing, ZG_2, 2)
ZG_3_predict = new_predict_label(ZG_str_testing, ZG_3, 3)
ZG_4_predict = new_predict_label(ZG_str_testing, ZG_4, 4)

SPY_2_predict = new_predict_label(SPY_str_testing, SPY_2, 2)
SPY_3_predict = new_predict_label(SPY_str_testing, SPY_3, 3)
SPY_4_predict = new_predict_label(SPY_str_testing, SPY_4, 4)


# Add the those predict label to dataframe
# convert string to list
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


ZG_testing.insert(loc=17, column="W2_label", value=Convert(ZG_2_predict))
ZG_testing.insert(loc=18, column="W3_label", value=Convert(ZG_3_predict))
ZG_testing.insert(loc=19, column="W4_label", value=Convert(ZG_4_predict))

SPY_testing.insert(loc=17, column="W2_label", value=Convert(SPY_2_predict))
SPY_testing.insert(loc=18, column="W3_label", value=Convert(SPY_3_predict))
SPY_testing.insert(loc=19, column="W4_label", value=Convert(SPY_4_predict))

print(f'For ZG:\n{ZG_testing}')
print(f'For SPY:\n{SPY_testing}')

print("\n ********************     Question 2.2    ******************* ")
# Calculate the accuracy
def accuracy(testing_str, predict_label):
    same = 0
    different = 0
    for i in range(len(testing_str)):
        if testing_str[i] == predict_label[i]:
            same += 1
        else:
            different += 1
        accuracy = same / (same + different)
    return accuracy

# put all the results in the dictionary
ZG_accuracy = {2: accuracy(ZG_str_testing, ZG_2_predict), 3: accuracy(ZG_str_testing, ZG_3_predict),
               4: accuracy(ZG_str_testing, ZG_4_predict)}
SPY_accuracy = {2: accuracy(SPY_str_testing, SPY_2_predict), 3: accuracy(SPY_str_testing, SPY_3_predict),
                4: accuracy(SPY_str_testing, SPY_4_predict)}
# output
print(f'For ZG, when K=2, the accuracy of true labels have I predicted correctly for the last two years is {ZG_accuracy[2]:.4f}'
      f'\nFor ZG, when K=3,the accuracy of true labels have I predicted correctly for the last two years is {ZG_accuracy[3]:.4f}'
      f'\nFor ZG, when K=4, the accuracy of true labels have I predicted correctly for the last two years is {ZG_accuracy[4]:.4f}'
      f'\nFor SPY, when K=2, the accuracy of true labels have I predicted correctly for the last two years is {SPY_accuracy[2]:.4f}'
      f'\nFor SPY, when K=3, the accuracy of true labels have I predicted correctly for the last two years is {SPY_accuracy[3]:.4f}'
      f'\nFor SPY, when K=4, the accuracy of true labels have I predicted correctly for the last two years is {SPY_accuracy[4]:.4f}')


print("\n ********************     Question 2.3    ******************* ")
def highest_accuracy(dict):
    value = dict.values()
    value_list = list(value)
    highest_value = max(value_list)
    # print(highest_value)
    for k, y in dict.items():
        if dict[k] == highest_value:
            print(f'When W = {k}, the accuracy is highest,which is {highest_value:.4f}.')


print(f'For ZG stock:')
highest_accuracy(ZG_accuracy)
print(f'For SPY stock:')
highest_accuracy(SPY_accuracy)

