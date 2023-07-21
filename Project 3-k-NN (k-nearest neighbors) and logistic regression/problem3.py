import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

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
print("\n ********************     Question 3.1 and 3.2    ******************* ")
ks = [3, 5, 7, 9, 11]
accuracies = []
for k in ks:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train_scaled, y_train)
    pred = knn_classifier.predict(X_test_scaled)
    acc = np.mean(pred == y_test)
    print("When k = {}, the accuracy is {}".format(k, acc))
    accuracies.append(acc)

acc_score = pd.DataFrame(
    {'k': ks,
     'acc': accuracies})

sns.lineplot(data=acc_score, x="k", y="acc")
plt.show()

# Find the optimal value of k
optimal_k = ks[np.argmax(accuracies)]
print("The optimal value of k is: ", optimal_k)

# Train the k-NN classifier using the optimal value of k and compute its performance measures
knn_classifier = KNeighborsClassifier(n_neighbors=optimal_k)
knn_classifier.fit(X_train_scaled, y_train)
prediction = knn_classifier.predict(X_test_scaled)
TP = np.sum((prediction == 1) & (y_test == 1))
FP = np.sum((prediction == 1) & (y_test == 0))
TN = np.sum((prediction == 0) & (y_test == 0))
FN = np.sum((prediction == 0) & (y_test == 1))
accuracy = (TP + TN) / (TP + FP + TN + FN)
TPR = TP / (TP + FN)
TNR = TN / (TN + FP)

performance_measures = pd.DataFrame({"TP": [TP],"FP": [FP],"TN": [TN],"FN": [FN],"accuracy": [accuracy],"TPR": [TPR],"TNR": [TNR]})
print("\n ********************     Question 3.3   ******************* ")
print(performance_measures)

# Compare the k-NN classifier with the simple classifier based on accuracy
simple_classifier_acc = np.mean(test['class'] == 0)
knn_classifier_acc = np.mean(prediction == y_test)
print("\n ********************     Question 3.4   ******************* ")
print("Accuracy of simple classifier:", simple_classifier_acc)
print("Accuracy of k-NN classifier:", knn_classifier_acc)

# Predict the class label for a new instance using both classifiers
new_instance = np.asarray([[0, 3, 3, 4]])
new_instance_scaled = scaler.transform(new_instance)
prediction = knn_classifier.predict(new_instance_scaled)
simple_classifier_prediction = 0
print("\n ********************     Question 3.5   ******************* ")
print("Class by simple classifier is", simple_classifier_prediction)
print("Class label predicted for the new instance by k-NN classifier is {}".format(prediction[0]))

