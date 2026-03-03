# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Internship Task 02 – Prodigy Infotech

This project implements K-Means Clustering to perform customer segmentation based on spending behavior and annual income.

The objective is to group customers into distinct clusters to better understand purchasing patterns and target marketing strategies effectively.

---

## 📊 Dataset Used

Mall Customers Dataset

Features selected for clustering:

* Annual Income (k$)
* Spending Score (1–100)

---

## 🧠 Problem Statement

Unsupervised learning was applied to identify natural groupings within the dataset without predefined labels.

K-Means clustering was used to:

* Determine optimal number of clusters using the Elbow Method
* Segment customers into 5 distinct groups

---

## ⚙️ Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## 📈 Implementation Steps

1. Data loading and feature selection
2. Elbow Method to determine optimal k
3. K-Means model training
4. Cluster visualization using scatter plots

---

## 🔍 Key Insights

* Customers can be segmented into 5 groups based on income and spending score.
* Certain clusters represent high-income high-spenders (premium customers).
* Some clusters represent low-income low-spenders (budget segment).

These insights can help businesses design targeted marketing strategies.

---

## 📁 Project Structure

Task2_KMeans/
│
├── task2_kmeans.py
├── Mall_Customers.csv
└── README.md

---

## 🚀 How to Run

1. Install required libraries:
   pip install pandas matplotlib scikit-learn

2. Run the script:
   python task2_kmeans.py

---

## 🎯 Conclusion

This project demonstrates the practical implementation of unsupervised machine learning using K-Means Clustering and highlights how data-driven customer segmentation can support strategic business decisions.
