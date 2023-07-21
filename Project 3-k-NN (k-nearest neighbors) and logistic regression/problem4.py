import pandas as pd
import numpy as np
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

ks = [3, 5, 7, 9, 11]
accuracies = []
for k in ks:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train_scaled, train['class'].values)
    pred = knn_classifier.predict(X_test_scaled)
    acc = np.mean(pred ==  test['class'].values)
    print("When k = {}, the accuracy is {}".format(k, acc))
    accuracies.append(acc)

acc_score = pd.DataFrame(
    {'k': ks,
     'acc': accuracies})


# select best k
best_k = ks[np.argmax(accuracies)]
print("The best value of k is", best_k)
print("\n ********************     Question 4.1   ******************* ")
# train k-NN classifier on all 4 features
knn_classifier = KNeighborsClassifier(n_neighbors=best_k)
knn_classifier.fit(X_train_scaled, train['class'].values)

# define X_train_scaled and X_test_scaled with only 3 features
X_train_scaled_truncated = np.delete(X_train_scaled, [0, 1, 2], axis=1)
X_test_scaled_truncated = np.delete(X_test_scaled, [0, 1, 2], axis=1)

# calculate accuracy for each truncated feature set
feature_names = ['variance', 'skewness', 'curtosis', 'entropy']
truncated_accuracies = []
for i in range(4):
    X_train_truncated = np.delete(train.loc[:, train.columns != 'class'].values, i, axis=1)
    X_test_truncated = np.delete(test.loc[:, test.columns != 'class'].values, i, axis=1)
    scaler_truncated = StandardScaler().fit(X_train_truncated)
    X_train_scaled_truncated = scaler_truncated.transform(X_train_truncated)
    X_test_scaled_truncated = scaler_truncated.transform(X_test_truncated)
    knn_classifier.fit(X_train_scaled_truncated, train['class'].values)
    pred_truncated = knn_classifier.predict(X_test_scaled_truncated)
    acc_truncated = np.mean(pred_truncated == test['class'].values)
    truncated_accuracies.append(acc_truncated)
    print("Accuracy with feature {} removed: {}".format(feature_names[i], acc_truncated))
print("\n ********************     Question 4.2 and 4.3 and 4.4   ******************* ")
# compare accuracies with and without each feature
print("\n Feature removed | Change in accuracy")
print("------------------------------------")
for i in range(4):
    change_in_acc = accuracies[-1] - truncated_accuracies[i]
    print("{} | {}".format(feature_names[i], change_in_acc))


print("\nWhen variance removed, contributed the most to loss of accuracy")
print("When entropy removed, contributed the least to loss of accuracy")
