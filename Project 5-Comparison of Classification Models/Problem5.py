import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Read the data and drop rows with missing values
df = pd.read_excel('CTG.xls', sheet_name='Raw Data')
df = df[['MSTV', 'Width', 'Mode', 'Variance', 'NSP']].dropna()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['MSTV', 'Width', 'Mode', 'Variance']], df['NSP'], test_size=0.3, random_state=1)

# Create a Naive Bayes classifier and fit it to the training data
nb = GaussianNB()
nb.fit(X_train, y_train)

# Create a Decision Tree classifier and fit it to the training data
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Create a Random Forest classifier and fit it to the training data
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Predict the labels of the test data using each model
nb_preds = nb.predict(X_test)
dt_preds = dt.predict(X_test)
rf_preds = rf.predict(X_test)

# Compute the confusion matrix for each model
nb_cm = confusion_matrix(y_test, nb_preds)
dt_cm = confusion_matrix(y_test, dt_preds)
rf_cm = confusion_matrix(y_test, rf_preds)

# Compute the True Positive Rate and True Negative Rate for each model
nb_tpr = nb_cm[0,0]/(nb_cm[0,0]+nb_cm[0,1])
nb_tnr = nb_cm[1,1]/(nb_cm[1,0]+nb_cm[1,1])
dt_tpr = dt_cm[0,0]/(dt_cm[0,0]+dt_cm[0,1])
dt_tnr = dt_cm[1,1]/(dt_cm[1,0]+dt_cm[1,1])
rf_tpr = rf_cm[0,0]/(rf_cm[0,0]+rf_cm[0,1])
rf_tnr = rf_cm[1,1]/(rf_cm[1,0]+rf_cm[1,1])

# Compute the overall accuracy for each model
nb_acc = np.mean(nb_preds == y_test)
dt_acc = np.mean(dt_preds == y_test)
rf_acc = np.mean(rf_preds == y_test)
print("\n ********************     Question 5.1    ******************* ")
# Print the results in a table
results = pd.DataFrame({'Model': ['Naive Bayesian', 'Decision Tree', 'Random Forest'],
                        'TP': [nb_cm[0,0], dt_cm[0,0], rf_cm[0,0]],
                        'FP': [nb_cm[0,1], dt_cm[0,1], rf_cm[0,1]],
                        'TN': [nb_cm[1,1], dt_cm[1,1], rf_cm[1,1]],
                        'FN': [nb_cm[1,0], dt_cm[1,0], rf_cm[1,0]],
                        'accuracy': [nb_acc, dt_acc, rf_acc],
                        'TPR': [nb_tpr, dt_tpr, rf_tpr],
                        'TNR': [nb_tnr, dt_tnr, rf_tnr]})
print(results)
print("\n ********************      Discuss findings    ******************* ")
print("\nThe model with the highest accuracy is Random Forest and the model with "
      "\nthe lowest accuracy is the  Naive Bayesian. Similarly, TPR is highest "
      "\nin Random Forest and lowest in Naive Bayes.")