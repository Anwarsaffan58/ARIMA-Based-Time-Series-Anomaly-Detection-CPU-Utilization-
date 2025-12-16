"""
PROJECT: ARIMA CPU Anomaly Detection
AUTHOR: Saffan
DESCRIPTION: 
    This script simulates server CPU traffic, trains an ARIMA statistical model 
    to learn normal patterns, and detects anomalies (spikes/crashes) 
    using a dynamic threshold (2.5 standard deviations).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
import warnings

# Suppress warnings for cleaner CMD output
warnings.filterwarnings("ignore")

# ==========================================
# CONFIGURATION & SETUP
# ==========================================
CONFIG = {
    'data_path': 'data/cpu_data.csv',
    'plot_path': 'outputs/detection_plot.png',
    'report_path': 'outputs/anomaly_report.csv',
    'days': 30,
    'hours_per_day': 24,
    'anomaly_threshold': 2.5,  # Standard Deviations
    'arima_order': (5, 1, 0)   # (p,d,q) - Tuned for this synthetic pattern
}

def ensure_directories():
    """Creates necessary folders if they don't exist."""
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)

# ==========================================
# PART 1: DATA GENERATION
# ==========================================
def generate_synthetic_data():
    """
    Generates 720 hours (30 days) of CPU data with:
    - Daily seasonality (Sine wave)
    - Random noise
    - 5 Injected Anomalies
    """
    print("[1/5] Generating synthetic CPU dataset...")
    
    np.random.seed(42)
    total_hours = CONFIG['days'] * CONFIG['hours_per_day']
    
    # Time index
    time = np.arange(total_hours)
    
    # Base Signal: Sine wave (Daily cycle) + Trend
    seasonality = 10 * np.sin(2 * np.pi * time / 24) 
    trend = 0.05 * time
    noise = np.random.normal(0, 2, total_hours)
    
    cpu_usage = 40 + seasonality + trend + noise
    
    # Inject Anomalies (Spikes and Drops)
    anomalies_indices = [50, 120, 300, 550, 680]
    for idx in anomalies_indices:
        cpu_usage[idx] += np.random.choice([30, -25]) # Spike up or crash down
    
    # Clip to 0-100% range
    cpu_usage = np.clip(cpu_usage, 0, 100)
    
    # Create DataFrame
    dates = pd.date_range(start='2024-01-01', periods=total_hours, freq='H')
    df = pd.DataFrame({'timestamp': dates, 'cpu_percent': cpu_usage})
    
    # Save to CSV
    df.to_csv(CONFIG['data_path'], index=False)
    print(f"      Data saved to {CONFIG['data_path']}")
    return df

# ==========================================
# PART 2: MODEL TRAINING (ARIMA)
# ==========================================
def train_and_detect(df):
    """
    Fits ARIMA model and detects anomalies using residual analysis.
    """
    print(f"[2/5] Training ARIMA{CONFIG['arima_order']} model...")
    
    # Train/Test Split (Use all data for anomaly detection context)
    series = df['cpu_percent']
    
    # Fit ARIMA Model
    model = ARIMA(series, order=CONFIG['arima_order'])
    model_fit = model.fit()
    
    print(f"      Model AIC: {model_fit.aic:.2f}")
    
    # Calculate Residuals (Actual - Predicted)
    print("[3/5] Calculating residuals and detecting anomalies...")
    df['predicted'] = model_fit.predict(start=0, end=len(df)-1)
    df['residual'] = df['cpu_percent'] - df['predicted']
    
    # Define Dynamic Threshold
    residual_mean = df['residual'].mean()
    residual_std = df['residual'].std()
    upper_threshold = residual_mean + (CONFIG['anomaly_threshold'] * residual_std)
    lower_threshold = residual_mean - (CONFIG['anomaly_threshold'] * residual_std)
    
    # Flag Anomalies
    df['is_anomaly'] = ((df['residual'] > upper_threshold) | 
                        (df['residual'] < lower_threshold))
    
    anomaly_count = df['is_anomaly'].sum()
    print(f"      Detected {anomaly_count} anomalies (Threshold: {CONFIG['anomaly_threshold']}σ)")
    
    return df, model_fit

# ==========================================
# PART 3: VISUALIZATION & REPORTING
# ==========================================
def visualize_results(df):
    """
    Plots the Actual vs Predicted CPU usage and highlights anomalies.
    """
    print("[4/5] Generating visualization...")
    
    plt.figure(figsize=(14, 7))
    
    # Plot Actual Data
    plt.plot(df['timestamp'], df['cpu_percent'], label='Actual CPU %', color='#1f77b4', alpha=0.7)
    
    # Plot Predicted Data
    plt.plot(df['timestamp'], df['predicted'], label='ARIMA Predicted', color='#ff7f0e', linestyle='--')
    
    # Highlight Anomalies
    anomalies = df[df['is_anomaly']]
    plt.scatter(anomalies['timestamp'], anomalies['cpu_percent'], 
                color='red', s=100, label='Anomaly Detected', zorder=5)
    
    plt.title(f"Server CPU Anomaly Detection (ARIMA)\nThreshold: {CONFIG['anomaly_threshold']} Sigma | Anomalies Found: {len(anomalies)}")
    plt.ylabel('CPU Utilization (%)')
    plt.xlabel('Timestamp')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save Plot
    plt.savefig(CONFIG['plot_path'])
    print(f"      Plot saved to {CONFIG['plot_path']}")
    plt.close()

def save_report(df):
    """
    Saves only the anomalous records to a CSV file.
    """
    print("[5/5] Saving anomaly report...")
    anomalies = df[df['is_anomaly']]
    anomalies.to_csv(CONFIG['report_path'], index=False)
    print(f"      Report saved to {CONFIG['report_path']}")

# ==========================================
# MAIN PIPELINE EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- STARTING CPU ANOMALY DETECTION PIPELINE ---\n")
    
    ensure_directories()
    
    # 1. Load Data
    data = generate_synthetic_data()
    
    # 2. Train & Detect
    results, model = train_and_detect(data)
    
    # 3. Visualize
    visualize_results(results)
    
    # 4. Save
    save_report(results)
    
    print("\n--- PIPELINE COMPLETE ---")
    print(f"Check the '{os.path.dirname(CONFIG['plot_path'])}' folder for results.")