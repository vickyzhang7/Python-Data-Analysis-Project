import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read the data from the file
df = pd.read_csv("data_banknote_authentication.txt", sep=",", header=None)
df.columns = ["f1", "f2", "f3", "f4", "class"]

# Define the list of features
features = ["f1", "f2", "f3", "f4"]

# Create an empty dictionary to store the accuracies
accuracies = {}

# Loop over each feature
for feature in features:
    # Remove the feature from both Xtrain and Xtest
    X_train = df.drop([feature, 'class'], axis=1).values
    X_test = df.drop([feature, 'class'], axis=1).values
    y_train = df['class'].values
    y_test = df['class'].values

    # Fit a logistic regression model on the truncated Xtrain
    lr_classifier = LogisticRegression()
    lr_classifier.fit(X_train, y_train)

    # Make predictions on Xtest using the fitted model
    predictions = lr_classifier.predict(X_test)

    # Compute the accuracy and store it in the dictionary
    accuracies[feature] = accuracy_score(y_test, predictions)
print("\n ********************     Question 6.1   ******************* ")
# Print the accuracies for each feature
for feature, accuracy in accuracies.items():
    print(f"Accuracy without {feature}: {accuracy:.4f}")
print("\n ********************     Question 6.2   ******************* ")
# Compute the accuracy with all features
X_train = df.drop(['class'], axis=1).values
X_test = df.drop(['class'], axis=1).values
y_train = df['class'].values
y_test = df['class'].values
lr_classifier = LogisticRegression()
lr_classifier.fit(X_train, y_train)
predictions = lr_classifier.predict(X_test)
accuracy_all_features = accuracy_score(y_test, predictions)
print(f"Accuracy with all features: {accuracy_all_features:.4f}")
print("\n ********************     Question 6.3   ******************* ")
# Find the feature that contributed the most to loss of accuracy
max_loss_feature = max(accuracies, key=lambda x: accuracy_all_features - accuracies[x])
print(f"The feature that contributed the most to loss of accuracy: {max_loss_feature}")
print("\n ********************     Question 6.4   ******************* ")
# Find the feature that contributed the least to loss of accuracy
min_loss_feature = min(accuracies, key=lambda x: accuracy_all_features - accuracies[x])
print(f"The feature that contributed the least to loss of accuracy: {min_loss_feature}")

print("\n ********************     Question 6.1   ******************* ")
print("The relative significance of features obtained using logistic regression is different from that obtained using k-NN,"
      "\nwhere k-NN found that the entropy feature was the most significant.")
