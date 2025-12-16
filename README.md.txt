# 📈 ARIMA CPU Anomaly Detection

A time-series analysis tool designed to detect server performance anomalies (CPU spikes and crashes) using statistical modeling.

## 🚀 Project Overview
This tool simulates 30 days of server CPU usage data, trains an **ARIMA (AutoRegressive Integrated Moving Average)** model to learn the "normal" usage pattern, and flags deviations that exceed a dynamic statistical threshold.

### Key Features
- **Synthetic Data Engine**: Generates realistic 720-hour datasets with seasonality, trend, and noise.
- **Statistical Detection**: Uses Residual Analysis (Actual - Predicted) with a **2.5σ (Standard Deviation)** threshold.
- **Automated Reporting**: Outputs a visual plot and a CSV report of all detected incidents.

## 🛠️ Installation & Usage

1. **Clone the repository** (or create the folder structure).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt