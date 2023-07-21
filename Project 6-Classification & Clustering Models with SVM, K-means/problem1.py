import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the dataset
df = pd.read_csv('seeds_dataset.csv', header=None)
df.columns = ['area', 'perimeter', 'compactness', 'kernel_length', 'kernel_width', 'asymmetry_coeff', 'kernel_groove_length', 'class']

# Select the two classes based on the remainder of your building's last digit
df = df[df['class'].isin([2, 3])]


# Split the dataset into training and testing sets
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)


# Linear kernel SVM
svm_linear = SVC(kernel='linear', random_state=42)
svm_linear.fit(X_train, y_train)
y_pred_linear = svm_linear.predict(X_test)
acc_linear = accuracy_score(y_test, y_pred_linear)
cm_linear = confusion_matrix(y_test, y_pred_linear)

# Gaussian kernel SVM
svm_gaussian = SVC(kernel='rbf', random_state=42)
svm_gaussian.fit(X_train, y_train)
y_pred_gaussian = svm_gaussian.predict(X_test)
acc_gaussian = accuracy_score(y_test, y_pred_gaussian)
cm_gaussian = confusion_matrix(y_test, y_pred_gaussian)

# Polynomial kernel SVM of degree 3
svm_poly = SVC(kernel='poly', degree=3, random_state=42)
svm_poly.fit(X_train, y_train)
y_pred_poly = svm_poly.predict(X_test)
acc_poly = accuracy_score(y_test, y_pred_poly)
cm_poly = confusion_matrix(y_test, y_pred_poly)
print("\n ********************     Question 1.1    ******************* ")
# Linear kernel SVM
print('Linear kernel SVM')
print('Accuracy:', acc_linear)
print('Confusion matrix:\n', cm_linear)
print("\n ********************     Question 1.2    ******************* ")
# Gaussian kernel SVM
print('\nGaussian kernel SVM')
print('Accuracy:', acc_gaussian)
print('Confusion matrix:\n', cm_gaussian)
print("\n ********************     Question 1.3    ******************* ")
# Polynomial kernel SVM of degree 3
print('\nPolynomial kernel SVM of degree 3')
print('Accuracy:', acc_poly)
print('Confusion matrix:\n', cm_poly)

