"""
Oasis Infobyte - Data Science Internship (OIBSIP)
Task 4: Email Spam Detection with Machine Learning
Author: Aditya (Intern)
"""

import os
import re
import string
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    text = re.sub(r'<.*?>+', ' ', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub(r'\w*\d\w*', ' ', text)
    return " ".join([w for w in text.split() if len(w) > 2])

def main():
    print("="*75)
    print("  OASIS INFOBYTE SIP - TASK 4: EMAIL/SMS SPAM DETECTION (NLP)  ")
    print("="*75)
    
    data_path = os.path.join(os.path.dirname(__file__), "dataset", "spam.csv")
    df = pd.read_csv(data_path)
    
    print("\n[1] Class Distribution:")
    print(df['v1'].value_counts())
    
    df['cleaned'] = df['v2'].apply(clean_text)
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    
    X_train, X_test, y_train, y_test = train_test_split(df['cleaned'], df['label'], test_size=0.20, random_state=42, stratify=df['label'])
    
    tfidf = TfidfVectorizer(max_features=2500, ngram_range=(1, 2))
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)
    
    models = {
        "Multinomial Naive Bayes": MultinomialNB(alpha=0.2),
        "Logistic Regression": LogisticRegression(random_state=42),
        "Linear Support Vector (SVC)": LinearSVC(random_state=42, dual=False),
        "Random Forest Classifier": RandomForestClassifier(n_estimators=100, random_state=42)
    }
    
    print("\n[2] NLP Classifier Benchmark Results:")
    print("-" * 65)
    print(f"{'Classifier':<32} {'Accuracy':<10} {'Precision':<12} {'Recall':<10}")
    print("-" * 65)
    
    for name, model in models.items():
        model.fit(X_train_vec, y_train)
        preds = model.predict(X_test_vec)
        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds)
        rec = recall_score(y_test, preds)
        print(f"{name:<32} {acc*100:>7.2f}%   {prec:>10.4f}   {rec:>8.4f}")
        
    print("-" * 65)
    print("\n[SUCCESS] Pipeline executed successfully.")

if __name__ == "__main__":
    main()
