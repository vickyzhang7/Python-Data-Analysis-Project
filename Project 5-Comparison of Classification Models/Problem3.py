import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the data into a Pandas dataframe
df = pd.read_excel('CTG.xls', sheet_name='Raw Data')

# Prepare the data by removing unwanted columns and dropping rows with missing values
df = df[['MSTV', 'Width', 'Mode', 'Variance', 'NSP']].dropna()
print("\n ********************     Question 3.1    ******************* ")
print("Split my set 50/50")
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.5, random_state=42)

# Create and train the decision tree classifier
dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train, y_train)

# Predict the classes for the test data
y_pred = dtc.predict(X_test)

# Compute the accuracy and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
print("\n ********************     Question 3.2    ******************* ")
print("Accuracy: ", accuracy)
print("\n ********************     Question 3.3    ******************* ")
print("Confusion matrix:\n", confusion)
