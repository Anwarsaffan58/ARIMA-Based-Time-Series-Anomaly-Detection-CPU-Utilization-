# 📈 ARIMA CPU Anomaly Detection

A robust time-series analysis tool designed to detect server performance anomalies (unexpected CPU spikes and crashes) using statistical modeling.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Maintained-brightgreen)

## 🚀 Project Overview
In modern DevOps and SRE environments, manual monitoring of server metrics is impossible. This project automates health monitoring by:
1. **Simulating** 30 days of realistic server CPU usage (720 hourly data points).
2. **Training** an **ARIMA (AutoRegressive Integrated Moving Average)** model to learn the "normal" daily traffic patterns.
3. **Detecting** anomalies by calculating the deviation between *expected* behavior and *actual* behavior.

### 🔑 Key Features
- **Synthetic Data Engine**: Generates realistic time-series data with seasonality (daily cycles), trends, and random noise.
- **Statistical Detection**: Implements a dynamic threshold using **Residual Analysis** (Threshold: > 2.5 Standard Deviations).
- **Automated Reporting**: Instantly generates a visual plot (`.png`) and a CSV log (`.csv`) of all flagged incidents.
- **Production Ready**: Structured modular pipeline (Load → Train → Detect → Report).

## 🛠️ Tech Stack
- **Python 3.x**
- **Statsmodels**: For ARIMA modeling and statistical analysis.
- **Pandas/NumPy**: For high-performance data manipulation.
- **Matplotlib**: For data visualization.

- pip install -r requirements.txt
- python main.py
expected output
--- STARTING CPU ANOMALY DETECTION PIPELINE ---

[1/5] Generating synthetic CPU dataset...
      Data saved to data/cpu_data.csv
[2/5] Training ARIMA(5, 1, 0) model...
      Model AIC Score: 4112.77
[3/5] Detecting anomalies...
      Detected 12 anomalies (Threshold: 2.5 sigma)
[4/5] Generating visualization...
      Plot saved to outputs/detection_plot.png
[5/5] Saving anomaly report...
      Report saved to outputs/anomaly_report.csv

--- PIPELINE COMPLETE ---
Check the 'outputs' folder for results.
📊 Sample Results
The following metrics were achieved during a standard 30-day simulation:

Model Fit (AIC): 4112.77

Anomalies Detected: 12 (Sensitivity: 2.5σ)

Visualization: The system successfully flagged injected "attacks" (sudden 30% spikes) and "server crashes" (sudden drops), distinguishing them from normal daily fluctuations.

🧠 How It Works (The Logic)
Stationarity: The system removes the upward trend to stabilize the mean.

ARIMA(5,1,0): The model looks at the past 5 hours of data to predict the next hour.

Residual Check: Residual = Actual_Value - Predicted_Value.

Z-Score Thresholding: If the residual is greater than 2.5x the standard deviation of errors, the timestamp is marked as an anomaly.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📝 Author
Saffan

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/Anwarsaffan58/ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-.git](https://github.com/Anwarsaffan58/ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-.git)
cd ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-
