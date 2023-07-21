
from problem3 import *
print("\n ********************     Question 4.1    ******************* ")
# TP - true positives (your predicted label is + and true label is +)
def TP(data, true_label, predict_label):
    TP = 0
    for i in range(len(data)):
        if data[predict_label].values[i] == data[true_label].values[i] == "+":
            TP += 1
    return TP


# FP - false positives (your predicted label is + but true label is − )
def FP(data, true_label, predict_label):
    FP = 0
    for i in range(len(data)):
        if data[predict_label].values[i] == "+" and data[true_label].values[i] == "-"  :
            FP += 1
    return FP


# TN - true negatives (your predicted label is − and true label is − )
def TN(data, true_label, predict_label):
    TN = 0
    for i in range(len(data)):
        if data[predict_label].values[i] == data[true_label].values[i] == "-":
            TN += 1
    return TN


# FN - false negatives (your predicted label is − but true label is +
def FN(data, true_label, predict_label):
    FN = 0
    for i in range(len(data)):
        if data[predict_label].values[i] == "-" and data[true_label].values[i] == "+" :
            FN += 1
    return FN


# TPR = TP/(TP + FN) - true positive rate.
def TPR(data, true_label, predict_label):
    TPR = TP(data, true_label, predict_label) / (
            TP(data, true_label, predict_label) + FN(data, true_label, predict_label))
    TPR=round(TPR,4)
    return TPR


# TNR = TN/(TN + FP) - true negative rate.
def TNR(data, true_label, predict_label):
    TNR = TN(data, true_label, predict_label) / (
            TN(data, true_label, predict_label) + FP(data, true_label, predict_label))
    TNR = round(TNR, 4)
    return TNR


def all_results(data, true_label, predict_label):
    key_list = ["TP", "FP", "TN", "FN", "TPR", "TNR"]
    value_list = [TP(data, true_label, predict_label), FP(data, true_label, predict_label),
                  TN(data, true_label, predict_label),
                  FN(data, true_label, predict_label), TPR(data, true_label, predict_label),
                  TNR(data, true_label, predict_label)]
    all_results = dict(zip(key_list, value_list))
    return all_results


ZG_W2_confusion_matrix = all_results(ZG_testing, 'True_label', 'W2_label')
ZG_W2_confusion_matrix['Accuracy'] = ZG_accuracy[2]
ZG_W3_confusion_matrix = all_results(ZG_testing, 'True_label', 'W3_label')
ZG_W3_confusion_matrix['Accuracy'] = ZG_accuracy[3]
ZG_W4_confusion_matrix = all_results(ZG_testing, 'True_label', 'W4_label')
ZG_W4_confusion_matrix['Accuracy'] = ZG_accuracy[4]
ZG_ensemble_confusion_matrix = all_results(ZG_testing, 'True_label', 'ensemble_label')
ZG_ensemble_confusion_matrix['Accuracy'] = ZG_ensemble_accuracy

SPY_W2_confusion_matrix = all_results(SPY_testing, 'True_label', 'W2_label')
SPY_W2_confusion_matrix['Accuracy'] = SPY_accuracy[2]
SPY_W3_confusion_matrix = all_results(SPY_testing, 'True_label', 'W3_label')
SPY_W3_confusion_matrix['Accuracy'] = SPY_accuracy[3]
SPY_W4_confusion_matrix = all_results(SPY_testing, 'True_label', 'W4_label')
SPY_W4_confusion_matrix['Accuracy'] = SPY_accuracy[4]
SPY_ensemble_confusion_matrix = all_results(SPY_testing, 'True_label', 'ensemble_label')
SPY_ensemble_confusion_matrix['Accuracy'] = SPY_ensemble_accuracy



# create list of results for each dataset
ZG_results = [['2', 'ZG', ZG_W2_confusion_matrix['TP'], ZG_W2_confusion_matrix['FP'],
               ZG_W2_confusion_matrix['TN'], ZG_W2_confusion_matrix['FN'], ZG_accuracy[2],
               ZG_W2_confusion_matrix['TPR'], ZG_W2_confusion_matrix['TNR']],
              ['3', 'ZG', ZG_W3_confusion_matrix['TP'], ZG_W3_confusion_matrix['FP'],
               ZG_W3_confusion_matrix['TN'], ZG_W3_confusion_matrix['FN'], ZG_accuracy[3],
               ZG_W3_confusion_matrix['TPR'], ZG_W3_confusion_matrix['TNR']],
              ['4', 'ZG', ZG_W4_confusion_matrix['TP'], ZG_W4_confusion_matrix['FP'],
               ZG_W4_confusion_matrix['TN'], ZG_W4_confusion_matrix['FN'], ZG_accuracy[4],
               ZG_W4_confusion_matrix['TPR'], ZG_W4_confusion_matrix['TNR']],
              ['Ensemble', 'ZG', ZG_ensemble_confusion_matrix['TP'], ZG_ensemble_confusion_matrix['FP'],
               ZG_ensemble_confusion_matrix['TN'], ZG_ensemble_confusion_matrix['FN'], ZG_ensemble_accuracy,
               ZG_ensemble_confusion_matrix['TPR'], ZG_ensemble_confusion_matrix['TNR']],
             ['2', 'SPY', SPY_W2_confusion_matrix['TP'], SPY_W2_confusion_matrix['FP'],
               SPY_W2_confusion_matrix['TN'], SPY_W2_confusion_matrix['FN'], SPY_accuracy[2],
               SPY_W2_confusion_matrix['TPR'], SPY_W2_confusion_matrix['TNR']],
              ['3', 'SPY', SPY_W3_confusion_matrix['TP'], SPY_W3_confusion_matrix['FP'],
               SPY_W3_confusion_matrix['TN'], SPY_W3_confusion_matrix['FN'], SPY_accuracy[3],
               SPY_W3_confusion_matrix['TPR'], SPY_W3_confusion_matrix['TNR']],
              ['4', 'SPY', SPY_W4_confusion_matrix['TP'], SPY_W4_confusion_matrix['FP'],
               SPY_W4_confusion_matrix['TN'], SPY_W4_confusion_matrix['FN'], SPY_accuracy[4],
               SPY_W4_confusion_matrix['TPR'], SPY_W4_confusion_matrix['TNR']],
              ['Ensemble', 'SPY', SPY_ensemble_confusion_matrix['TP'], SPY_ensemble_confusion_matrix['FP'],
               SPY_ensemble_confusion_matrix['TN'], SPY_ensemble_confusion_matrix['FN'], SPY_ensemble_accuracy,
               SPY_ensemble_confusion_matrix['TPR'], SPY_ensemble_confusion_matrix['TNR']]]

# create pandas dataframe from results list
df = pd.DataFrame(ZG_results, columns=['W', 'Ticker', 'TP', 'FP', 'TN', 'FN', 'Accuracy', 'TPR', 'TNR'])

# print dataframe as string
print(df.to_string(index=False))
print("\n ********************     Question 4.2    ******************* ")

print("My Find:"
      "\n 1.for both my ticker and SPY, the true result is usually higher than false result,that means accuracy higher than 0.5, except w=2 and ensemble for ZG;"
      "\n 2.for both my ticker and SPY, the positive result is usually higher than negative result,that means TPR higher than TNR,except w=2 for my ticker;"
      "\n 3.the accuracy and true positive result of SPY are higher than that of my ticker. ")