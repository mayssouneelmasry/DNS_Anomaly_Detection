DNS Anomaly Detection System
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/scikit--learn-1.0+-orange.svg
https://img.shields.io/badge/License-MIT-green.svg

📋 Overview
A comprehensive DNS anomaly detection system that identifies malicious patterns in DNS traffic using unsupervised machine learning algorithms. This project focuses on detecting DNS cache poisoning attacks by analyzing query volumes, TTL values, and transaction ID entropy.

🎯 Problem Statement
DNS (Domain Name System) is critical internet infrastructure that translates domain names to IP addresses. However, it is vulnerable to DNS Cache Poisoning (DNS Spoofing) attacks where attackers inject fake DNS responses into resolver caches, redirecting users to malicious websites.

Key Attack Consequences:
🎣 Phishing attacks

🦠 Malware distribution

⚡ Service disruption

🔍 Solution Approach
Our system monitors DNS traffic patterns and detects anomalies using three unsupervised learning algorithms:

Isolation Forest - Isolates anomalies by randomly partitioning data

K-Means Clustering - Identifies outliers based on distance from cluster centroids

One-Class SVM - Learns decision boundary for normal data

📊 Dataset
The project uses synthetic DNS traffic data with the following features:

Feature	Description	Data Type
Timestamp	Exact time of DNS query/response	DateTime
Source_IP	IP address of requesting device	IPv4/IPv6
Destination_IP	DNS server IP address	IPv4/IPv6
Query_Volume	Number of DNS queries per period	Integer
TTL_Value	Cache validity duration (seconds)	Integer
Transaction_ID_Entropy	Randomness measure of transaction IDs	Float (0-1)
Selected Features for Anomaly Detection:
Query_Volume - Detects unusual traffic patterns (DDoS, flooding attacks)

TTL_Value - Identifies suspicious low TTL values (cache manipulation)

Transaction_ID_Entropy - Detects predictable TXIDs (spoofing attempts)

🏗️ Project Structure
text
dns-anomaly-detection/
│
├── data/
│   └── synthetic_dns_traffic.csv          # DNS traffic dataset
│
├── results/
│   ├── isolation_forest_results.csv       # IF predictions
│   ├── kmeans_results.csv                 # K-Means predictions
│   └── ocsvm_results.csv                  # OCSVM predictions
│
├── DNS_Detection.py                        # Main detection script
├── DNS_Anomaly_Detection.pptx              # Project presentation
└── README.md                               # Documentation
🚀 Installation
bash
# Clone the repository
git clone https://github.com/yourusername/dns-anomaly-detection.git
cd dns-anomaly-detection

# Install required packages
pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn
💻 Usage
Running the Detection Pipeline
python
# Execute the main detection script
python DNS_Detection.py
Expected Output:
CSV files containing anomaly detection results for each model

Visualization comparing model performance (Precision, Recall, F1-Score)

Console output with performance metrics

📈 Model Performance Comparison
Model	Precision	Recall	F1-Score	Generalization
Isolation Forest	Highest	Highest	Highest	❌ Overfitting
K-Means	High	High	High	✅ Good
One-Class SVM	Lowest	Lowest	Lowest	❌ Poor
Key Findings:
Isolation Forest achieved the best scores but suffers from overfitting, limiting performance on unseen data

K-Means delivers consistent performance with good generalization - RECOMMENDED FOR PRODUCTION

One-Class SVM struggles with data complexity and is not recommended

📊 Visualization
https://Anomaly%2520Detection%2520Model%2520comparison.jpg

The comparison chart shows performance metrics across all three models, clearly demonstrating Isolation Forest's superior scores and K-Means' balanced performance.

🎯 Conclusion & Recommendations
After comprehensive testing and analysis:

Production Recommendation: K-Means Clustering offers the optimal balance of performance and generalization, making it the most reliable choice for real-world DNS anomaly detection.

Isolation Forest can be used when maximum detection accuracy is needed and overfitting can be mitigated through cross-validation.

One-Class SVM is not recommended for this use case due to poor performance.

🔧 Future Improvements
Implement cross-validation to address Isolation Forest overfitting

Add real-time DNS traffic monitoring capability

Integrate with popular DNS servers (BIND, Unbound)

Develop alerting system for detected anomalies

Expand feature set with additional DNS metrics

👥 Team
Maryam Waheed Zamel (ID: 2205154)

Amina Ahmed Ferra (ID: 2205225)

Mayssoune Hussein ElMasry (ID: 2205251)

Hanin Mohamed Hamouda (ID: 2205232)

📚 Technologies Used
Python 3.8+ - Core programming language

scikit-learn - Machine learning algorithms

pandas - Data manipulation and analysis

numpy - Numerical computing

matplotlib/seaborn - Data visualization

imbalanced-learn - Handling imbalanced datasets

🙏 Acknowledgments
Special thanks to our instructors for guidance on DNS security and anomaly detection methodologies.

