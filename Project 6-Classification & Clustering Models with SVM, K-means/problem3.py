import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix

print("\n ********************     Question 3.1    ******************* ")

df = pd.read_csv('seeds_dataset.csv', header=None)
df.columns = ['area', 'perimeter', 'compactness', 'kernel_length', 'kernel_width', 'asymmetry_coeff', 'kernel_groove_length', 'class']

# Separate the features and class label
X = df.drop('class', axis=1)
Y = df['class']

distortions = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, n_init=10).fit(X)
    distortions.append(kmeans.inertia_)

plt.plot(range(1, 8), distortions, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Distortion')
plt.show()

# Determine the best k using the "knee" method
knee = np.diff(distortions, 2)
optimal_k = knee.argmax() + 2

print(f"The optimal number of clusters is {optimal_k}")

print("\n ********************     Question 3.2    ******************* ")
# Select two random features
fi, fj = np.random.choice(X.columns, size=2, replace=False)

# Fit the k-means model with the optimal k
kmeans = KMeans(n_clusters=optimal_k, n_init=10).fit(X)
y_km = kmeans.fit_predict(X)


# Plot the data points and centroids
plt.scatter(X[fi], X[fj], c=Y)
plt.scatter(kmeans.cluster_centers_[:, X.columns.get_loc(fi)],
            kmeans.cluster_centers_[:, X.columns.get_loc(fj)],
            s=200, marker='*', c='k')
plt.xlabel(fi)
plt.ylabel(fj)
plt.title(f'Clusters using {fi} and {fj}')
plt.show()

print("Generally, the value of class2 feature will be larger. The value of the class3 feature is smaller. "
      "\nIn several pairs of random features, the distribution of three classes will form a linear relationship, "
      "\nsuch as f2 and f5, f1 and f5. Other pairs were more dispersed, such as f2 and f3, and f3 and f4.")


print("\n ********************     Question 3.3    ******************* ")
# Running KMeans clustering for k=2
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=20)
kmeans.fit(X[[fi, fj]])

# Assigning a cluster label based on majority class of items
labels = []
for i in range(optimal_k):
    cluster_indices = kmeans.labels_ == i
    cluster = Y[cluster_indices]
    label = cluster.value_counts().idxmax()
    labels.append(label)

# Printing out centroid and assigned label for each cluster
for i, centroid in enumerate(kmeans.cluster_centers_):
    print("Cluster", i+1, "Centroid:", centroid, "Assigned label:", labels[i])


print("\n ********************     Question 3.4    ******************* ")
import numpy as np
from scipy.spatial.distance import cdist

# Selecting largest 3 clusters with labels 1, 2, and 3
A_indices = kmeans.labels_ == 0
B_indices = kmeans.labels_ == 1
C_indices = kmeans.labels_ == 2

A = X[A_indices]
B = X[B_indices]
C = X[C_indices]

# Calculating centroids of A, B, and C clusters
mu_A = np.mean(A, axis=0)
mu_B = np.mean(B, axis=0)
mu_C = np.mean(C, axis=0)

# Assigning labels based on nearest centroid
distances = cdist(X, np.array([mu_A, mu_B, mu_C]), metric='euclidean')
labels = np.argmin(distances, axis=1) + 1

# Calculating overall accuracy
overall_accuracy = (labels == Y).mean()
print("Overall accuracy:", overall_accuracy)


print("\n ********************     Question 3.5    ******************* ")
# Subset the data to include only labels 1 and 2
subset_data = df[df['class'].isin([1, 2])].copy()

# Get the features and labels
X = subset_data.drop('class', axis=1)
Y = subset_data['class']

# Assign labels based on nearest centroid
predictions = []
for i in range(len(X)):
    point = X.iloc[i,:]
    distances = [np.linalg.norm(point - centroid) for centroid in [mu_A, mu_B]]
    nearest_centroid_label = np.argmin(distances) + 1
    predictions.append(nearest_centroid_label)

# Calculate accuracy and confusion matrix
accuracy = accuracy_score(Y, predictions)
cm = confusion_matrix(Y, predictions)
print('Accuracy:', accuracy)
print('Confusion Matrix:\n', cm)
print('\n Findings:The acccuracy of the new classifier is smaller than the previous classifiers.')


