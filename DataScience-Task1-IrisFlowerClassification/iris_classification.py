"""
Oasis Infobyte - Data Science Internship (OIBSIP)
Task 1: Iris Flower Classification
Author: Aditya (Intern)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    print("="*70)
    print("  OASIS INFOBYTE SIP - TASK 1: IRIS FLOWER CLASSIFICATION  ")
    print("="*70)
    
    # 1. Load Dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    df['species'] = [iris.target_names[i] for i in iris.target]
    
    print("\n[1] Exploratory Data Analysis (EDA):")
    print(f"Dataset Shape: {df.shape}")
    print(f"Missing Values: {df.isnull().sum().sum()}")
    print("\nDescriptive Statistics:")
    print(df.describe().round(2))
    print("\nClass Distribution:")
    print(df['species'].value_counts())
    
    # 2. Features and Split
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[features]
    y = df['species']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n[2] Data Split: Train samples = {len(X_train)}, Test samples = {len(X_test)}")
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 3. Model Training & Comparison
    models = {
        "Logistic Regression": (LogisticRegression(max_iter=200, random_state=42), True),
        "K-Nearest Neighbors (K=5)": (KNeighborsClassifier(n_neighbors=5), True),
        "Decision Tree": (DecisionTreeClassifier(max_depth=3, random_state=42), False),
        "Random Forest": (RandomForestClassifier(n_estimators=100, random_state=42), False),
        "Support Vector Machine (Linear)": (SVC(kernel='linear', random_state=42), True)
    }
    
    print("\n[3] Model Benchmark Results:")
    print("-" * 65)
    print(f"{'Classifier':<32} {'Accuracy':<12} {'Macro F1':<10}")
    print("-" * 65)
    
    best_acc = 0.0
    best_model_name = ""
    best_report = None
    best_cm = None
    
    for name, (clf, use_scaled) in models.items():
        X_tr = X_train_scaled if use_scaled else X_train
        X_te = X_test_scaled if use_scaled else X_test
        
        clf.fit(X_tr, y_train)
        preds = clf.predict(X_te)
        acc = accuracy_score(y_test, preds)
        rep = classification_report(y_test, preds, output_dict=True)
        cm = confusion_matrix(y_test, preds)
        
        print(f"{name:<32} {acc*100:>8.2f}%    {rep['macro avg']['f1-score']:>8.4f}")
        
        if acc > best_acc:
            best_acc = acc
            best_model_name = name
            best_report = rep
            best_cm = cm
            
    print("-" * 65)
    print(f"\n[4] Selected Best Model: {best_model_name} with {best_acc*100:.2f}% Accuracy")
    print(f"\nDetailed Classification Report for {best_model_name}:")
    print(pd.DataFrame(best_report).T.round(3))
    
    print("\nConfusion Matrix:")
    print(best_cm)
    print("\n[SUCCESS] Pipeline executed successfully.")

if __name__ == "__main__":
    main()
