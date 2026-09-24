"""
Oasis Infobyte - Data Science Internship (OIBSIP)
Task 5: Sales Prediction Using Python
Author: Aditya (Intern)
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

def main():
    print("="*75)
    print("  OASIS INFOBYTE SIP - TASK 5: ADVERTISING SALES PREDICTION  ")
    print("="*75)
    
    data_path = os.path.join(os.path.dirname(__file__), "dataset", "Advertising.csv")
    df = pd.read_csv(data_path)
    
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    models = {
        "Linear Regression (Baseline)": LinearRegression(),
        "Polynomial Regression (Degree 2)": make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    print("\n[1] Sales Forecasting Benchmark Results:")
    print("-" * 65)
    print(f"{'Model':<35} {'MAE ($k)':<12} {'RMSE':<10} {'R² Score':<10}")
    print("-" * 65)
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        rmse = root_mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)
        print(f"{name:<35} {mae:>8.3f}    {rmse:>6.3f}    {r2:>8.4f}")
        
    print("-" * 65)
    
    # Channel Attribution
    lr = models["Linear Regression (Baseline)"]
    print("\n[2] Channel Budget Attribution (Coefficients):")
    print(f"  * TV Spend Coefficient        : +{lr.coef_[0]:.4f} sales units per $1k spend")
    print(f"  * Radio Spend Coefficient     : +{lr.coef_[1]:.4f} sales units per $1k spend")
    print(f"  * Newspaper Spend Coefficient : +{lr.coef_[2]:.4f} sales units per $1k spend")
    print(f"\nConclusion: Radio offers the highest marginal unit return per dollar (+{lr.coef_[1]:.4f}), closely followed by TV (+{lr.coef_[0]:.4f}). Newspaper spend exhibits negligible impact.")
    print("\n[SUCCESS] Pipeline executed successfully.")

if __name__ == "__main__":
    main()
