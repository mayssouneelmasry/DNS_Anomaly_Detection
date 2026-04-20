# DNS Anomaly Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Overview

A comprehensive DNS anomaly detection system that identifies malicious patterns in DNS traffic using unsupervised machine learning algorithms. This project focuses on detecting DNS cache poisoning attacks by analyzing query volumes, TTL values, and transaction ID entropy.

---

## 🎯 Problem Statement

DNS (Domain Name System) is critical internet infrastructure that translates domain names to IP addresses. However, it is vulnerable to **DNS Cache Poisoning (DNS Spoofing)** attacks where attackers inject fake DNS responses into resolver caches, redirecting users to malicious websites.

### Key Attack Consequences:

| Consequence | Description |
|-------------|-------------|
| 🎣 Phishing | Users redirected to fake login pages |
| 🦠 Malware Distribution | Malicious code delivered via compromised domains |
| ⚡ Service Disruption | Legitimate services become unavailable |

---

## 🔍 Solution Approach

Our system monitors DNS traffic patterns and detects anomalies using three unsupervised learning algorithms:

| Algorithm | Method |
|-----------|--------|
| **Isolation Forest** | Isolates anomalies by randomly partitioning data |
| **K-Means Clustering** | Identifies outliers based on distance from cluster centroids |
| **One-Class SVM** | Learns decision boundary for normal data |

---

## 📊 Dataset

The project uses synthetic DNS traffic data with the following features:

| Feature | Description | Data Type |
|---------|-------------|-----------|
| `Timestamp` | Exact time of DNS query/response | DateTime |
| `Source_IP` | IP address of requesting device | IPv4/IPv6 |
| `Destination_IP` | DNS server IP address | IPv4/IPv6 |
| `Query_Volume` | Number of DNS queries per period | Integer |
| `TTL_Value` | Cache validity duration (seconds) | Integer |
| `Transaction_ID_Entropy` | Randomness measure of transaction IDs | Float (0-1) |

### Selected Features for Anomaly Detection:

- **Query_Volume** - Detects unusual traffic patterns (DDoS, flooding attacks)
- **TTL_Value** - Identifies suspicious low TTL values (cache manipulation)
- **Transaction_ID_Entropy** - Detects predictable TXIDs (spoofing attempts)

---

## 🏗️ Project Structure

- **dns-anomaly-detection/**
  - **data/**
    - `synthetic_dns_traffic.csv` - DNS traffic dataset
  - **results/**
    - `isolation_forest_results.csv` - IF predictions
    - `kmeans_results.csv` - K-Means predictions
    - `ocsvm_results.csv` - OCSVM predictions
  - `DNS_Detection.py` - Main detection script
  - `DNS_Anomaly_Detection.pptx` - Project presentation
  - `Anomaly Detection Model comparison.jpg` - Performance chart
  - `README.md` - Documentation

---


| File | Description |
|------|-------------|
| `synthetic_dns_traffic.csv` | Synthetic DNS traffic dataset with 6 features |
| `isolation_forest_results.csv` | Anomaly detection results from Isolation Forest model |
| `kmeans_results.csv` | Anomaly detection results from K-Means model |
| `ocsvm_results.csv` | Anomaly detection results from One-Class SVM model |
| `DNS_Detection.py` | Main Python script for running all detection models |
| `DNS_Anomaly_Detection.pptx` | Project presentation slides |
| `Anomaly Detection Model comparison.jpg` | Performance visualization chart |
| `README.md` | Project documentation |

---

## 🚀 Installation

# Clone the repository
git clone https://github.com/yourusername/dns-anomaly-detection.git
cd dns-anomaly-detection

# Install required packages
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn


## 💻 Usage

### Running the Detection Pipeline

python DNS_Detection.py

### Expected Output:

1. CSV files containing anomaly detection results for each model
2. Visualization comparing model performance (Precision, Recall, F1-Score)
3. Console output with performance metrics


## 📈 Model Performance Comparison

| Model | Precision | Recall | F1-Score | Generalization |
|-------|-----------|--------|----------|----------------|
| Isolation Forest | Highest | Highest | Highest | ❌ Overfitting |
| K-Means | High | High | High | ✅ Good |
| One-Class SVM | Lowest | Lowest | Lowest | ❌ Poor |

### Key Findings:

- Isolation Forest achieved the best scores but suffers from overfitting, limiting performance on unseen data
- K-Means delivers consistent performance with good generalization - RECOMMENDED FOR PRODUCTION
- One-Class SVM struggles with data complexity and is not recommended


## 📊 Visualization

![Model Comparison](Anomaly%20Detection%20Model%20comparison.jpg)

The comparison chart shows performance metrics across all three models, clearly demonstrating Isolation Forest's superior scores and K-Means' balanced performance.


## 🎯 Conclusion & Recommendations

After comprehensive testing and analysis:

| Recommendation | Reason |
|----------------|--------|
| K-Means Clustering (Production) | Optimal balance of performance and generalization |
| Isolation Forest (Specific use cases) | Maximum detection accuracy when overfitting can be mitigated |
| One-Class SVM | Not recommended for this use case |


## 🔧 Future Improvements

- [ ] Implement cross-validation to address Isolation Forest overfitting
- [ ] Add real-time DNS traffic monitoring capability
- [ ] Integrate with popular DNS servers (BIND, Unbound)
- [ ] Develop alerting system for detected anomalies
- [ ] Expand feature set with additional DNS metrics


## 👥 Team

| Name | ID |
|------|-----|
| Maryam Waheed Zamel | 2205154 |
| Amina Ahmed Ferra | 2205225 |
| Mayssoune Hussein ElMasry | 2205251 |
| Hanin Mohamed Hamouda | 2205232 |


## 📚 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| scikit-learn | Machine learning algorithms |
| pandas | Data manipulation and analysis |
| numpy | Numerical computing |
| matplotlib/seaborn | Data visualization |
| imbalanced-learn | Handling imbalanced datasets |


## 📄 License

This project is licensed under the MIT License.


## 🙏 Acknowledgments

Special thanks to our instructors for guidance on DNS security and anomaly detection methodologies.


⭐ If you find this project useful, please consider giving it a star on GitHub!
