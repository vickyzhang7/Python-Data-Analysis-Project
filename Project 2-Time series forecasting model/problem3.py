from problem2 import *
print("\n ********************     Question 3.1    ******************* ")
ZG_training = my_stock[(my_stock['Year'] >= 2018) & (my_stock['Year'] <= 2020)]
ZG_testing = my_stock[(my_stock['Year'] >= 2020) & (my_stock['Year'] <= 2021)]
SPY_training = SPY[(SPY['Year'] >= 2018) & (SPY['Year'] <= 2020)]
SPY_testing = SPY[(SPY['Year'] >= 2020) & (SPY['Year'] <= 2021)]
def ensemble_label(predicted_2, predicted_3, predicted_4):
    # ensemble label is '-' when predict label is --+, -+-.+--,---
    ensembel_label = ""
    for i in range(len(predicted_2)):
        if predicted_2[i] == predicted_3[i] == "-":
            ensembel_label += "-"
        elif predicted_2[i] == predicted_4[i] == "-":
            ensembel_label += "-"
        elif predicted_3[i] == predicted_4[i] == "-":
            ensembel_label += "-"
        elif predicted_2[i] == predicted_3[i] == predicted_4[i] == "-":
            ensembel_label += "-"
        else:
            ensembel_label += "+"
    return ensembel_label


ZG_ensemble_label = ensemble_label(ZG_2_predict, ZG_3_predict, ZG_4_predict)
SPY_ensemble_label = ensemble_label(SPY_2_predict, SPY_3_predict,SPY_4_predict)

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

ZG_testing.insert(loc=17, column="W2_label", value=Convert(ZG_2_predict))
ZG_testing.insert(loc=18, column="W3_label", value=Convert(ZG_3_predict))
ZG_testing.insert(loc=19, column="W4_label", value=Convert(ZG_4_predict))
ZG_testing.insert(loc=20, column="ensemble_label", value=Convert(ZG_ensemble_label))
print("For ZG STOCK:")
print(ZG_testing[["True_label", "W2_label", "W3_label", "W4_label", "ensemble_label"]])

SPY_testing.insert(loc=17, column="W2_label", value=Convert(SPY_2_predict))
SPY_testing.insert(loc=18, column="W3_label", value=Convert(SPY_3_predict))
SPY_testing.insert(loc=19, column="W4_label", value=Convert(SPY_4_predict))
SPY_testing.insert(loc=20, column="ensemble_label", value=Convert(SPY_ensemble_label))
print("For SPY Stock:")
print(SPY_testing[["True_label", "W2_label", "W3_label", "W4_label", "ensemble_label"]])


print("\n ********************     Question 3.2    ******************* ")

def ensemble_accuracy(data, column1, column2):
    correct = 0
    wrong = 0
    for i in range(len(data)):
        if data[column1].values[i] == data[column2].values[i]:
            correct += 1
        else:
            wrong += 1
    return correct / (correct + wrong)

ZG_ensemble_accuracy = ensemble_accuracy(ZG_testing, "True_label", "ensemble_label")
SPY_ensemble_accuracy = ensemble_accuracy(SPY_testing, "True_label", "ensemble_label")

print(f'For the ZG STOCKS, the percentage of labels in year 4 and 5 I compute correctly by using ensemble is {ZG_ensemble_accuracy:.4f}')
print(f'For the SPY STOCKS, the percentage of labels in year 4 and 5 I compute correctly by using ensemble is {SPY_ensemble_accuracy:.4f}')

print("\n ********************     Question 3.3    ******************* ")


def Negative_or_Positive_accuracy(data, true_label, x, a, b):
    # check the negative accuracy of each predict label when a = '-' & b = '+'
    # check the postive accuracy of each predict label when a = '+' & b = '-'
    correct = 0
    wrong = 0
    for i in range(len(data)):
        if data[true_label].values[i] == data[x].values[i] == a:
            correct += 1
        elif data[true_label].values[i] == a and data[x].values[i] == b:
            wrong += 1
    return correct / (correct + wrong)


def improve_or_unimproved(x1, x2):
    if x1 > x2:
        return "improved"
    else:
        return "unimproved"


ZG_W2_Neg_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W2_label', "-", "+")
ZG_W3_Neg_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W3_label', "-", "+")
ZG_W4_Neg_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W4_label', "-", "+")
ZG_ensemble_Neg_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'ensemble_label', "-", "+")

ZG_W2_VS_EN_N = improve_or_unimproved(ZG_ensemble_Neg_Accuracy, ZG_W2_Neg_Accuracy)
ZG_W3_VS_EN_N = improve_or_unimproved(ZG_ensemble_Neg_Accuracy, ZG_W3_Neg_Accuracy)
ZG_W4_VS_EN_N = improve_or_unimproved(ZG_ensemble_Neg_Accuracy, ZG_W4_Neg_Accuracy)

print('\nFor the ZG STOCK:')
print(f'Compared to W=2, The accuracy on predicted "-" labels by using ensemble {ZG_W2_VS_EN_N}'
      f'\nCompared to W=3, The accuracy on predicted "-" labels by using ensemble {ZG_W3_VS_EN_N}'
      f'\nCompared to W=4, The accuracy on predicted "-" labels by using ensemble {ZG_W4_VS_EN_N}')

SPY_W2_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W2_label', "-", "+")
SPY_W3_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W3_label', "-", "+")
SPY_W4_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W4_label', "-", "+")
SPY_ensemble_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'ensemble_label', "-", "+")

SPY_W2_VS_EN_N = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W2_Neg_Accuracy)
SPY_W3_VS_EN_N = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W3_Neg_Accuracy)
SPY_W4_VS_EN_N = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W4_Neg_Accuracy)

print('\nFor the SPY STOCK:')
print(f'Compared to W=2, The accuracy on predicted "-" labels by using ensemble {SPY_W2_VS_EN_N}'
      f'\nCompared to W=3, The accuracy on predicted "-" labels by using ensemble {SPY_W3_VS_EN_N}'
      f'\nCompared to W=4, The accuracy on predicted "-" labels by using ensemble {SPY_W4_VS_EN_N}')

print("\n ********************     Question 3.4    ******************* ")
ZG_W2_Pos_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W2_label', "+", "-")
ZG_W3_Pos_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W3_label', "+", "-")
ZG_W4_Pos_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'W4_label', "+", "-")
ZG_ensemble_Pos_Accuracy = Negative_or_Positive_accuracy(ZG_testing, 'True_label', 'ensemble_label', "+", "-")

ZG_W2_VS_EN_P = improve_or_unimproved(ZG_ensemble_Pos_Accuracy, ZG_W2_Pos_Accuracy)
ZG_W3_VS_EN_P = improve_or_unimproved(ZG_ensemble_Pos_Accuracy, ZG_W3_Pos_Accuracy)
ZG_W4_VS_EN_P = improve_or_unimproved(ZG_ensemble_Pos_Accuracy, ZG_W4_Pos_Accuracy)

print(f'\nFor the ZG STOCK:')
print(f'Compared to W=2, The accuracy on predicted "+" labels by using ensemble {ZG_W2_VS_EN_P},'
      f'\nCompared to W=3, The accuracy on predicted "+" labels by using ensemble {ZG_W3_VS_EN_P},'
      f'\nCompared to W=4, The accuracy on predicted "+" labels by using ensemble {ZG_W4_VS_EN_P}.')

SPY_W2_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W2_label', "+", "-")
SPY_W3_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W3_label', "+", "-")
SPY_W4_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'W4_label', "+", "-")
SPY_ensemble_Neg_Accuracy = Negative_or_Positive_accuracy(SPY_testing, 'True_label', 'ensemble_label', "+", "-")

SPY_W2_VS_EN_P = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W2_Neg_Accuracy)
SPY_W3_VS_EN_P = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W3_Neg_Accuracy)
SPY_W4_VS_EN_P = improve_or_unimproved(SPY_ensemble_Neg_Accuracy, SPY_W4_Neg_Accuracy)

print(f'\nFor the SPY STOCK:')
print(f'Compared to W=2, The accuracy on predicted "+" labels by using ensemble {SPY_W2_VS_EN_P},'
      f'\nCompared to W=3, The accuracy on predicted "+" labels by using ensemble {SPY_W3_VS_EN_P},'
      f'\nCompared to W=4, The accuracy on predicted "+" labels by using ensemble {SPY_W4_VS_EN_P}.')

