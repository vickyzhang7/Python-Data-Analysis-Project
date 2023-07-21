import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load data into dataframe
df = pd.read_csv("data_banknote_authentication.txt", header=None)
df.columns = ["f1", "f2", "f3", "f4", "class"]

# Add color column
df["color"] = df["class"].apply(lambda x: "green" if x == 0 else "red")

# Compute mean and standard deviation for each feature and class
class_stats = df.drop("color", axis=1).groupby("class").agg(["mean", "std"])[[("f1", "mean"), ("f2", "mean"), ("f3", "mean"), ("f4", "mean"), ("f1", "std"), ("f2", "std"), ("f3", "std"), ("f4", "std")]]
all_stats = df.drop("color", axis=1).groupby("class").agg(["mean", "std"])[[("f1", "mean"), ("f2", "mean"), ("f3", "mean"), ("f4", "mean"), ("f1", "std"), ("f2", "std"), ("f3", "std"), ("f4", "std")]]


# Split dataset into training and testing sets
X = df.drop("class", axis=1)
y = df["class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=500)

# Plot pairwise relationships for training data
good_bills = X_train[y_train == 0]
sns.pairplot(good_bills, hue="color", diag_kind="hist")
plt.savefig("good_bills.pdf")
plt.clf()

fake_bills = X_train[y_train == 1]
sns.pairplot(fake_bills, hue="color", diag_kind="hist")
plt.savefig("fake_bills.pdf")
plt.clf()

# Define simple classifier
def simple_classifier(row):
    if row["f1"] > 0 and row["f2"] > 2 and row["f4"] < 2.5:
        return 0
    else:
        return 1

# Apply simple classifier to test data
print("\n ********************     Question 2.3    ******************* ")
y_pred = X_test.apply(simple_classifier, axis=1)
print(y_pred)

# Compute TP, FP, TN, FN, TPR, and TNR
TP = sum((y_pred == 0) & (y_test == 0))
FP = sum((y_pred == 0) & (y_test == 1))
TN = sum((y_pred == 1) & (y_test == 1))
FN = sum((y_pred == 1) & (y_test == 0))
accuracy = (TP + TN) / (TP + FP + TN + FN)
TPR = TP / (TP + FN)
TNR = TN / (TN + FP)

# Print results
print("\n ********************     Question 2.4 and 2.5    ******************* ")
results = pd.DataFrame({"TP": [TP],"FP": [FP],"TN": [TN],"FN": [FN],"accuracy": [accuracy],"TPR": [TPR],"TNR": [TNR]})
print(results)


print("\n ********************     Question 2.6    ******************* ")
if(accuracy>0.5):
    print(f"\n Yes,Our simple classifier accuracy is {accuracy:.4f} doing better than coin flipping")
else:
    print(f"\n No,Our simple classifier accuracy is {accuracy:.4f} not doing better than coin flipping")
