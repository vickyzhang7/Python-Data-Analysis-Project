import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("data_banknote_authentication.txt", sep=",", header=None)
df.columns = ["f1", "f2", "f3", "f4", "class"]

train = df.sample(frac=0.5, random_state=500)
test = df.drop(train.index)

X_train = train.loc[:, train.columns != 'class'].values
X_test = test.loc[:, test.columns != 'class'].values
y_train = train['class'].values
y_test = test['class'].values

scaler = StandardScaler().fit(df.loc[:, df.columns != 'class'].values)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n ********************     Question 5.1   ******************* ")
LR_classifier = LogisticRegression()
LR_classifier.fit(X_train_scaled, y_train)
test_accuracy = LR_classifier.score(X_test_scaled, y_test)
print("Accuracy on X test is {}".format(test_accuracy))

print("\n ********************     Question 5.2   ******************* ")
prediction = LR_classifier.predict(X_test_scaled)
tn, fp, fn, tp = confusion_matrix(y_test, prediction).ravel()
accuracy = (tp + tn) / (tp + tn + fp + fn)
tpr = tp / (tp + fn)
tnr = tn / (tn + fp)
results = pd.DataFrame({'TP': [tp], 'FP': [fp], 'TN': [tn], 'FN': [fn],
                        'Accuracy': [accuracy], 'TPR': [tpr], 'TNR': [tnr]})
print(results)

print("\n ********************     Question 5.3   ******************* ")
knn_classifier = KNeighborsClassifier(n_neighbors=7)
knn_classifier.fit(X_train_scaled, y_train)
knn_prediction = knn_classifier.predict(X_test_scaled)
knn_tn, knn_fp, knn_fn, knn_tp = confusion_matrix(y_test, knn_prediction).ravel()
knn_accuracy = (knn_tp + knn_tn) / (knn_tp + knn_tn + knn_fp + knn_fn)

if accuracy> 0.704082:
    print("Logistic Regression performs better than the simple classifier for accuracy.")
if tpr > 0.541772:
    print("Logistic Regression performs better than the simple classifier for TPR.")
if tnr > 0.924399:
    print("Logistic Regression performs better than the simple classifier for TNR.")
else:
    print("No, my logistic regression is not better than my simple classifier for any of the measures from the previous table")

print("\n ********************     Question 5.4   ******************* ")
if accuracy > 0.998542:
    print("Logistic Regression performs better than the k-NN classifier for accuracy.")
if tpr > 1.0:
    print("Logistic Regression performs better than the k-NN classifier for TPR.")
if tnr > 0.99275:
    print("Logistic Regression performs better than the k-NN classifier for TNR.")
else:
    print("No, my logistic regression is not better than my k-NN classifier for any of the measures from the previous table.")
print("\n ********************     Question 5.5   ******************* ")
bill = np.asarray([[0, 3, 3, 4]])
bill_scaled = scaler.transform(bill)
knn_prediction = knn_classifier.predict(bill_scaled)
lr_prediction = LR_classifier.predict(bill_scaled)
print("Class by Logistic Regression classifier is {}".format(lr_prediction[0]))
print("Class by k-NN classifier is {}".format(knn_prediction[0]))
