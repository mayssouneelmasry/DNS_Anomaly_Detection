# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.svm import OneClassSVM
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.model_selection import cross_val_score

# Load the DNS traffic dataset
file_path = "synthetic_dns_traffic.csv"  # Replace with your file path
dns_data = pd.read_csv(file_path)
print("Dataset loaded successfully. Sample data:")
print(dns_data.head())
print("No. of rows and columns : " , dns_data.shape)

# Select relevant features for anomaly detection
features = ['Query_Volume', 'TTL_Value', 'Transaction_ID_Entropy']
dns_features = dns_data[features]

# Scale the features using StandardScaler
scaler = StandardScaler()
dns_scaled = scaler.fit_transform(dns_features)

# ----- 1. Isolation Forest -----
iso_forest = IsolationForest(n_estimators=50, contamination=0.05 ,max_samples=0.8 , random_state=42)
dns_data['IF_Anomaly_Score'] = iso_forest.fit_predict(dns_scaled)
dns_data['IF_Anomaly'] = dns_data['IF_Anomaly_Score'] == -1
print(f"Total anomalies detected by Isolation Forest: {dns_data['IF_Anomaly'].sum()}")

# Save Isolation Forest results
if_results = dns_data.copy()
if_results.to_csv("isolation_forest_results.csv", index=False)
print("Isolation Forest results saved to 'isolation_forest_results.csv'.")

# Evaluate Isolation Forest
y_true = dns_data['IF_Anomaly'].astype(int)
y_pred = iso_forest.fit_predict(dns_scaled) == -1
precision_if = precision_score(y_true, y_pred)
recall_if = recall_score(y_true, y_pred)
f1_if = f1_score(y_true, y_pred)
print(f"Isolation Forest - Precision: {precision_if:.2f}, Recall: {recall_if:.2f}, F1-Score: {f1_if:.2f}")

# ----- 2. KMeans for Anomaly Detection -----
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(dns_scaled)

# Calculate distances to cluster centroids
distances = kmeans.transform(dns_scaled)
dns_data['KMeans_Anomaly_Score'] = np.min(distances, axis=1)

# Use a threshold to detect anomalies
threshold = np.percentile(dns_data['KMeans_Anomaly_Score'], 95)  # Top 5% are anomalies
dns_data['KMeans_Anomaly'] = dns_data['KMeans_Anomaly_Score'] > threshold
print(f"Total anomalies detected by KMeans: {dns_data['KMeans_Anomaly'].sum()}")

# Save KMeans results
kmeans_results = dns_data.copy()
kmeans_results.to_csv("kmeans_results.csv", index=False)
print("KMeans results saved to 'kmeans_results.csv'.")

# Evaluate KMeans
y_pred_kmeans = dns_data['KMeans_Anomaly'].astype(int)
precision_km = precision_score(y_true, y_pred_kmeans)
recall_km = recall_score(y_true, y_pred_kmeans)
f1_km = f1_score(y_true, y_pred_kmeans)
print(f"KMeans - Precision: {precision_km:.2f}, Recall: {recall_km:.2f}, F1-Score: {f1_km:.2f}")

# ----- 3. One-Class SVM -----
ocsvm = OneClassSVM(kernel='rbf', nu=0.05, gamma='scale')
ocsvm.fit(dns_scaled)

# Predict anomalies
dns_data['OCSVM_Anomaly'] = ocsvm.predict(dns_scaled)
dns_data['OCSVM_Anomaly'] = (dns_data['OCSVM_Anomaly'] == -1).astype(int)
print(f"Total anomalies detected by One-Class SVM: {dns_data['OCSVM_Anomaly'].sum()}")

# Save One-Class SVM results
ocsvm_results = dns_data.copy()
ocsvm_results.to_csv("ocsvm_results.csv", index=False)
print("One-Class SVM results saved to 'ocsvm_results.csv'.")

# Evaluate One-Class SVM
y_pred_ocsvm = dns_data['OCSVM_Anomaly'].astype(int)
precision_oc = precision_score(y_true, y_pred_ocsvm)
recall_oc = recall_score(y_true, y_pred_ocsvm)
f1_oc = f1_score(y_true, y_pred_ocsvm)
print(f"One-Class SVM - Precision: {precision_oc:.2f}, Recall: {recall_oc:.2f}, F1-Score: {f1_oc:.2f}")

# ----- Plot Comparison of Anomaly Detection Models -----
results = pd.DataFrame({
    'Model': ['Isolation Forest', 'KMeans', 'One-Class SVM'],
    'Precision': [precision_if, precision_km, precision_oc],
    'Recall': [recall_if, recall_km, recall_oc],
    'F1-Score': [f1_if, f1_km, f1_oc]
})

plt.figure(figsize=(10, 6))
bar_width = 0.25
index = np.arange(3)

plt.bar(index, results['Precision'], bar_width, label='Precision')
plt.bar(index + bar_width, results['Recall'], bar_width, label='Recall')
plt.bar(index + 2 * bar_width, results['F1-Score'], bar_width, label='F1-Score')

plt.xlabel('Model')
plt.ylabel('Score')
plt.title('Anomaly Detection Model Comparison')
plt.xticks(index + bar_width, results['Model'])
plt.legend()
plt.tight_layout()
plt.show()

# ----- Summary -----
print("\nModel Performance Summary:")
print(results)
