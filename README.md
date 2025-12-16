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

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/Anwarsaffan58/ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-.git](https://github.com/Anwarsaffan58/ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-.git)
cd ARIMA-Based-Time-Series-Anomaly-Detection-CPU-Utilization-
