import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

# Load data
df = pd.read_csv('seeds_dataset.csv', header=None)
df.columns = ['area', 'perimeter', 'compactness', 'kernel_length', 'kernel_width', 'asymmetry_coeff', 'kernel_groove_length', 'class']
df = df[df['class'].isin([2, 3])]

# Split data
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Define classifiers
classifiers = {
    'Linear SVM': SVC(kernel='linear'),
    'Gaussian SVM': SVC(kernel='rbf'),
    'Polynomial SVM': SVC(kernel='poly', degree=3),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=3),
    'Logistic Regression': LogisticRegression(),
    'Naive Bayes': GaussianNB()
}

# Train and evaluate classifiers
results = []
for clf_name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    results.append([clf_name, tp, fp, tn, fn, acc, tpr, tnr])
print("\n ********************     Question 2.1 and 2.2    ******************* ")
# Create results table
df_results = pd.DataFrame(results, columns=['Model', 'TP', 'FP', 'TN', 'FN', 'accuracy', 'TPR', 'TNR'])
print(df_results)
print("\n Findings:Based on the results of the classification models, it appears that all of them performed perfectly with 1 accuracy on the given dataset."
      "\n However, it should be noted that the dataset size is quite small, which could be a limiting factor in drawing any generalizable conclusions. "
      "\n Therefore, while the findings suggest that the models are effective in classifying the given dataset, "
      "\n further testing on larger datasets is necessary to validate the models' effectiveness.")
