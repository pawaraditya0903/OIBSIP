"""
Oasis Infobyte - Data Science Internship (OIBSIP)
Task 2: Unemployment Analysis with Python
Author: Aditya (Intern)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("="*75)
    print("  OASIS INFOBYTE SIP - TASK 2: UNEMPLOYMENT ANALYSIS IN INDIA (COVID-19)  ")
    print("="*75)
    
    # 1. Load Data
    data_path = os.path.join(os.path.dirname(__file__), "dataset", "Unemployment_in_India.csv")
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
    
    print("\n[1] Dataset Inspection:")
    print(f"Total Records: {len(df)}")
    print(f"Time Horizon: {df['Date'].min().strftime('%B %Y')} to {df['Date'].max().strftime('%B %Y')}")
    print(f"Missing Values: {df.isnull().sum().sum()}")
    print("\nSummary Statistics:")
    print(df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].describe().round(2))
    
    # 2. Regional Analysis
    print("\n[2] Top 5 States by Average Unemployment Rate:")
    top_states = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).head(5)
    for state, rate in top_states.items():
        print(f"  * {state:<22}: {rate:.2f}%")
        
    # 3. Macro Shock Analysis (Pre- vs Post-COVID)
    lockdown_date = pd.to_datetime("2020-03-24")
    df['Period'] = np.where(df['Date'] < lockdown_date, 'Pre-COVID', 'Post-COVID (Lockdown)')
    
    macro_comp = df.groupby('Period')[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].mean().round(2)
    print("\n[3] Pre-COVID vs Post-COVID Macroeconomic Comparison:")
    print(macro_comp)
    
    pre_rate = macro_comp.loc['Pre-COVID', 'Estimated Unemployment Rate (%)']
    post_rate = macro_comp.loc['Post-COVID (Lockdown)', 'Estimated Unemployment Rate (%)']
    pct_surge = ((post_rate - pre_rate) / pre_rate) * 100
    print(f"\nSurge in Mean Unemployment: +{pct_surge:.1f}% following the March 2020 lockdowns.")
    print("\n[SUCCESS] Pipeline executed successfully.")

if __name__ == "__main__":
    main()
