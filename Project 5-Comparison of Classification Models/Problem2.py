import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the Excel data into a Pandas dataframe
book = pd.read_excel('CTG.xls', sheet_name='Raw Data')

# Drop any rows that contain NaN values
book.dropna(inplace=True)

# Extract the features and target variable
X = book[['MSTV', 'Width', 'Mode', 'Variance']]
y = book['NSP']

# Split the data into training and testing sets
print("\n ********************     Question 2.1    ******************* ")
print("Split my set 50/50")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
# Train the Gaussian Naive Bayes model on the training data
gnb = GaussianNB()
gnb.fit(X_train, y_train)
# Predict the class labels for the testing data
y_pred = gnb.predict(X_test)
print("\n ********************     Question 2.2    ******************* ")
# Compute the accuracy of the model
acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)

# Compute the confusion matrix
print("\n ********************     Question 2.3    ******************* ")
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion matrix:\n{cm}")
