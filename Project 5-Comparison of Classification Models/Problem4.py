import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Load the data
df = pd.read_excel('CTG.xls', sheet_name='Raw Data')

# Prepare the data by removing unwanted columns and dropping rows with missing values
df = df[['MSTV', 'Width', 'Mode', 'Variance', 'NSP']].dropna()

# Split the data into training and testing sets
X = df[['MSTV', 'Width', 'Mode', 'Variance']]
y = df['NSP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Define the hyperparameters to be tested
N_values = range(1, 11)
d_values = range(1, 6)

# Initialize lists to store error rates and best N and d values
error_rates = []
best_N = 0
best_d = 0
best_error_rate = 1
print("\n ********************     Question 4.1    ******************* ")
# Loop over all values of N and d
for N in N_values:
    for d in d_values:
        # Train a random forest classifier with N trees and max depth d
        clf = RandomForestClassifier(n_estimators=N, max_depth=d, criterion='entropy')
        clf.fit(X_train, y_train)

        # Evaluate the classifier on the testing set and compute the error rate
        error_rate = 1 - clf.score(X_test, y_test)
        print(f'N={N}, d={d}, Error Rate={error_rate:.4f}')
        error_rates.append(error_rate)

        # Update the best N and d values if the current error rate is lower
        if error_rate < best_error_rate:
            best_N = N
            best_d = d
            best_error_rate = error_rate
print("\n ********************     Question 4.3    ******************* ")
# Print the best N and d values and the corresponding error rate
print(f"Best N value: {best_N}")
print(f"Best d value: {best_d}")
acc_rf = 1 - best_error_rate
print(f"Error rate for best N and d: {best_error_rate:.4f}")
print(f"Accuracy for best N and d: {acc_rf:.4f}")

# Plot the error rates for all combinations of N and d
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
cax = ax.matshow(np.array(error_rates).reshape(len(N_values), -1), cmap=plt.cm.Blues)

ax.set_xticks(range(len(d_values)))
ax.set_xticklabels(d_values)
ax.set_yticks(range(len(N_values)))
ax.set_yticklabels(N_values)
ax.set_xlabel('Max depth (d)')
ax.set_ylabel('Number of trees (N)')
ax.set_title('Random Forest Error Rates')

cbar = fig.colorbar(cax)
cbar.set_label('Error rate')

plt.show()

# Train a random forest classifier with the best N and d values
clf = RandomForestClassifier(n_estimators=best_N, max_depth=best_d, criterion='entropy')
clf.fit(X_train, y_train)

# Compute the confusion matrix for the testing set
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("\n ********************     Question 4.4    ******************* ")
print(f"Confusion matrix for best N and d:\n{cm}")
