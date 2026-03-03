# ==========================================
# Task 2: Customer Segmentation using K-Means
# ==========================================

print("STARTING TASK 2...")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)

# Select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# ------------------------------------------
# Step 1: Elbow Method
# ------------------------------------------
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# ------------------------------------------
# Step 2: Apply KMeans (k = 5)
# ------------------------------------------
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

# ------------------------------------------
# Step 3: Visualization
# ------------------------------------------
plt.figure()
plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)'],
    c=df['Cluster']
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()

print("\nTask 2 Completed Successfully ✅")