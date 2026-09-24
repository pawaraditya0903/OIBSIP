# 🚀 Oasis Infobyte SIP — Data Science Internship Repository (`OIBSIP`)

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-v1.9-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-v3.0-150458.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Internship-Completed-success.svg)](#)

This repository contains the complete portfolio of **5 industry-standard Data Science and Machine Learning projects** developed for the **Oasis Infobyte Student Internship Program (OIBSIP)** in the **Data Science Track**.

- **Intern Name:** Aditya
- **Internship Domain:** Data Science
- **Organization:** [Oasis Infobyte](https://oasisinfobyte.com/)
- **Repository Name:** `OIBSIP`

---

## 📂 Repository Architecture & Folder Structure

In strict adherence to Oasis Infobyte submission guidelines, each task is organized in its designated directory following the `OIBSIP/[TrackName]-[Level/Task]-[ProjectName]/` naming format:

```text
OIBSIP/
├── DataScience-Task1-IrisFlowerClassification/
│   ├── dataset/
│   │   └── iris.csv                                # Raw Morphological Dataset
│   ├── plots/
│   │   ├── pairplot.png                            # Feature Pairwise Distributions
│   │   ├── boxplots.png                            # Species Morphological Variance
│   │   ├── correlation_heatmap.png                 # Feature Correlation Matrix
│   │   ├── model_comparison.png                    # Classifier Accuracy Benchmark
│   │   └── confusion_matrix.png                    # Best Model Confusion Matrix
│   ├── iris_classification.py                      # Standalone Executable Python Pipeline
│   ├── DataScience_Task1_Iris_Classification.ipynb # Interactive Executed Jupyter Notebook
│   └── README.md                                   # Task Specification & Analysis Report
│
├── DataScience-Task2-UnemploymentAnalysis/
│   ├── dataset/
│   │   ├── Unemployment_in_India.csv               # Historical CMIE Regional Dataset
│   │   └── Unemployment_Rate_upto_11_2020.csv      # Monthly Series with Lockdown Shock
│   ├── plots/
│   │   ├── unemployment_timeseries.png             # Trajectory Across Key Indian States
│   │   ├── top10_states_unemployment.png           # Highest Average Unemployment Ranking
│   │   ├── correlation_heatmap.png                 # Macro Indicators Correlation
│   │   ├── precovid_vs_postcovid.png               # Pre vs Post COVID Distribution Boxplot
│   │   └── urban_vs_rural_impact.png               # Geographic Zone Disparities
│   ├── unemployment_analysis.py                    # Standalone Executable Python Pipeline
│   ├── DataScience_Task2_Unemployment_Analysis.ipynb # Interactive Executed Jupyter Notebook
│   └── README.md                                   # Macroeconomic Findings Report
│
├── DataScience-Task3-CarPricePrediction/
│   ├── dataset/
│   │   └── car_data.csv                            # Automotive Resale Dataset
│   ├── plots/
│   │   ├── price_distribution.png                  # Selling Price KDE & Histogram
│   │   ├── price_vs_age.png                        # Depreciation Trajectory Fit
│   │   ├── correlation_heatmap.png                 # Feature Correlation Heatmap
│   │   ├── feature_importance.png                  # Gini Importance Breakdown
│   │   ├── residuals_plot.png                      # Residual Error Diagnostics
│   │   └── model_comparison.png                    # R² Performance Benchmark
│   ├── car_price_prediction.py                     # Standalone Executable Python Pipeline
│   ├── DataScience_Task3_Car_Price_Prediction.ipynb # Interactive Executed Jupyter Notebook
│   └── README.md                                   # Valuation Modeling Report
│
├── DataScience-Task4-EmailSpamDetection/
│   ├── dataset/
│   │   └── spam.csv                                # SMS/Email Text Corpus
│   ├── plots/
│   │   ├── class_distribution.png                  # Spam vs Ham Class Ratio
│   │   ├── spam_wordcloud.png                      # Prominent Spam Keyword Clusters
│   │   ├── ham_wordcloud.png                       # Legitimate Communication Keywords
│   │   ├── confusion_matrices.png                  # Multi-Model Confusion Matrix Subplot
│   │   └── model_comparison.png                    # Precision/Recall/F1 Benchmarks
│   ├── spam_detection.py                           # Standalone Executable Python Pipeline
│   ├── DataScience_Task4_Email_Spam_Detection.ipynb # Interactive Executed Jupyter Notebook
│   └── README.md                                   # NLP Pipeline & Evaluation Report
│
├── DataScience-Task5-SalesPrediction/
│   ├── dataset/
│   │   └── Advertising.csv                         # Multi-Channel Ad Spend vs Sales
│   ├── plots/
│   │   ├── pairplot.png                            # Feature Distribution & Linearity
│   │   ├── scatter_channels.png                    # Individual Channel Regressions
│   │   ├── correlation_heatmap.png                 # Advertising Channel Correlations
│   │   ├── residual_plot.png                       # Regression Error Diagnostics
│   │   ├── actual_vs_predicted.png                 # Actual vs Predicted Sales Fit
│   │   └── model_comparison.png                    # R² Performance Benchmark
│   ├── sales_prediction.py                         # Standalone Executable Python Pipeline
│   ├── DataScience_Task5_Sales_Prediction.ipynb    # Interactive Executed Jupyter Notebook
│   └── README.md                                   # Marketing Attribution Report
│
├── DEMO_VIDEO_SCRIPT.md                            # Script & Title Card Guide for Submissions
├── LINKEDIN_POST_TEMPLATES.md                      # Pre-formatted LinkedIn Posts
├── SUBMISSION_GUIDE.md                             # Step-by-Step Certificate Checklist
├── title_card_generator.html                       # 2-Second Title Card Generator Tool
└── requirements.txt                                # Python Dependency Manifest
```

---

## 🏆 Project Portfolio & Results Summary

| Task # | Task Title | Primary Algorithms | Key Metrics | Champion Model |
|:---:|---|---|:---:|:---:|
| **Task 1** | **Iris Flower Classification** | Logistic Regression, KNN, Decision Tree, Random Forest, SVC | **100.00%** Test Accuracy | **Support Vector Machine (Linear)** |
| **Task 2** | **Unemployment Analysis with Python** | Time-Series EDA, Correlation Analysis, Macro Shock Modeling | **+210.5%** Peak Spike during COVID Lockdown | **Macro Impact Decomposition** |
| **Task 3** | **Car Price Prediction** | Linear Regression, Ridge, Random Forest, Gradient Boosting | **$R^2 = 95.39\%$**, MAE: ₹0.44L | **Gradient Boosting Regressor** |
| **Task 4** | **Email Spam Detection (NLP)** | Multinomial Naive Bayes, LinearSVC, Logistic Regression, RF | **100.00%** Accuracy, **1.00** Precision | **Multinomial Naive Bayes** |
| **Task 5** | **Sales Prediction Using Python** | Multivariate Linear Regression, Polynomial Reg, Random Forest | **$R^2 = 94.88\%$**, MAE: 0.781 | **Random Forest Regressor** |

---

## 🛠️ Environment Setup & Installation

To run any script or notebook locally:

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/OIBSIP.git
cd OIBSIP

# 2. Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download required NLTK corpora (for Task 4)
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

---

## 🎬 How to Execute Projects

### Running Standalone Python Pipelines:
```bash
# Task 1: Iris Classification
python DataScience-Task1-IrisFlowerClassification/iris_classification.py

# Task 2: Unemployment Analysis
python DataScience-Task2-UnemploymentAnalysis/unemployment_analysis.py

# Task 3: Car Price Prediction
python DataScience-Task3-CarPricePrediction/car_price_prediction.py

# Task 4: Spam Detection
python DataScience-Task4-EmailSpamDetection/spam_detection.py

# Task 5: Sales Prediction
python DataScience-Task5-SalesPrediction/sales_prediction.py
```

### Launching Jupyter Notebooks:
```bash
jupyter notebook
```
Navigate to any task directory and open the `.ipynb` file. All notebooks are pre-executed with rendered visualizations, data tables, and markdown insights.

---

## 📜 Oasis Infobyte Submission Documents
- [Submission Checklist & Guide](SUBMISSION_GUIDE.md)
- [Video Demo Walkthrough Script](DEMO_VIDEO_SCRIPT.md)
- [LinkedIn Post Templates](LINKEDIN_POST_TEMPLATES.md)
- [2-Second Title Card Generator](title_card_generator.html)

---

## 👤 Intern Information
- **Name:** Aditya
- **Internship:** Oasis Infobyte Student Internship Program (OIBSIP)
- **Domain:** Data Science
- **Batch:** September 2026
