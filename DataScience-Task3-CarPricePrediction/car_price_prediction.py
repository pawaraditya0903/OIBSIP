"""
Oasis Infobyte - Data Science Internship (OIBSIP)
Task 3: Car Price Prediction with Machine Learning
Author: Aditya (Intern)
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

def main():
    print("="*75)
    print("  OASIS INFOBYTE SIP - TASK 3: CAR PRICE PREDICTION (REGRESSION)  ")
    print("="*75)
    
    data_path = os.path.join(os.path.dirname(__file__), "dataset", "car_data.csv")
    df = pd.read_csv(data_path)
    
    # Feature Engineering
    current_year = 2026
    df['Car_Age'] = current_year - df['Year']
    
    # One-Hot Encoding
    df_encoded = pd.get_dummies(df[['Selling_Price', 'Present_Price', 'Kms_Driven', 'Car_Age', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']], drop_first=True)
    
    X = df_encoded.drop('Selling_Price', axis=1)
    y = df_encoded['Selling_Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=120, random_state=42),
        "Gradient Boosting Regressor": GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    print("\n[1] Regression Benchmark Results:")
    print("-" * 65)
    print(f"{'Model':<30} {'MAE (Lakhs)':<14} {'RMSE':<12} {'R² Score':<10}")
    print("-" * 65)
    
    best_r2 = -1.0
    best_name = ""
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        rmse = root_mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)
        print(f"{name:<30} {mae:>10.3f}    {rmse:>8.3f}   {r2:>8.4f}")
        if r2 > best_r2:
            best_r2 = r2
            best_name = name
            
    print("-" * 65)
    print(f"\n[2] Champion Model: {best_name} with R² = {best_r2:.4f}")
    print("\n[SUCCESS] Pipeline executed successfully.")

if __name__ == "__main__":
    main()
