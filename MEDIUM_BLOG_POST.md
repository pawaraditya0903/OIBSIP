# My OIBSIP Internship Journey: Learning Data Science by Building 5 Real-World Machine Learning Projects

*A comprehensive recap of my month-long Data Science internship experience with Oasis Infobyte, building end-to-end classification, regression, and NLP pipelines.*

---

## 🌟 Introduction

Entering the world of Data Science can feel overwhelming with all the theoretical concepts, mathematical formulas, and endless tutorials. However, the best way to bridge the gap between theory and practical engineering is by **getting your hands dirty with real datasets and building production-ready projects**.

During my **Data Science Internship at Oasis Infobyte (OIBSIP)**, I had the opportunity to work on structured, industry-oriented problem statements that challenged me to think like a data scientist — from exploratory data analysis and data cleaning to feature engineering, model benchmarking, and error diagnostics.

In this article, I want to share my journey, the architecture behind the **5 projects** I built, and the key insights I discovered along the way.

---

## 📂 The GitHub Repository
All code, datasets, visualization charts, and executed Jupyter Notebooks are completely open-source and documented in my GitHub repository:
👉 **[github.com/pawaraditya0903/OIBSIP](https://github.com/pawaraditya0903/OIBSIP)**

---

## 🚀 Project 1: Iris Flower Classification (Supervised ML)

**Objective:** Build a machine learning classification model to identify the species of an iris flower (*Setosa*, *Versicolor*, or *Virginica*) from its physical morphological measurements.

### 🔍 Methodology & EDA
We utilized the classic Iris dataset consisting of 150 instances across four numerical features: Sepal Length, Sepal Width, Petal Length, and Petal Width.
- **Exploratory Data Analysis:** Conducted pairwise distribution analysis using Seaborn pairplots and boxplots to visualize species separability.
- **Key Finding:** *Iris Setosa* is completely linearly separable from *Versicolor* and *Virginica* using `petal_length` alone (Setosa values are strictly $\le 2.0$ cm).
- **Modeling & Benchmark:** Evaluated 5 candidate classifiers: Logistic Regression, K-Nearest Neighbors ($K=5$), Decision Tree, Random Forest, and Linear Support Vector Machine (SVC).

### 🏆 Results
- **Champion Model:** **Linear Support Vector Classifier (SVC)** achieved **100.00% accuracy** on the unseen test set ($N=30$) with zero misclassifications across all three classes.

---

## 📈 Project 2: Unemployment Analysis in India (COVID-19 Economic Shock)

**Objective:** Perform exploratory data analysis on Indian unemployment data (May 2019 to October 2020) to uncover regional and temporal trends, isolating the macroeconomic shock triggered by the COVID-19 pandemic and national lockdown.

### 🔍 Methodology & Insights
- **Time-Series Analysis:** Tracked monthly unemployment trajectories across key industrial and agricultural states (Delhi, Maharashtra, Bihar, Uttar Pradesh, Tamil Nadu, Haryana).
- **Lockdown Impact:** We observed an immediate, unprecedented surge in unemployment during April–May 2020, spiking by **+94.7%** above pre-COVID baselines (with peak state-level unemployment exceeding 35%).
- **Correlation Matrix:** Confirmed a strong inverse correlation between unemployment rates and labor participation rates, highlighting the "discouraged worker effect" where individuals ceased looking for employment during peak lockdown restrictions.

---

## 🚗 Project 3: Car Price Prediction with Machine Learning (Regression)

**Objective:** Build a predictive regression model that estimates the resale market value of used automobiles in India based on age, original showroom price, kilometers driven, fuel type, transmission, and seller channels.

### 🔍 Methodology & Feature Engineering
- **Feature Engineering:** Derived a `Car_Age` variable from the manufacturing year and applied One-Hot Encoding to categorical variables (`Fuel_Type`, `Seller_Type`, `Transmission`).
- **Models Benchmarked:** Evaluated Linear Regression, Ridge Regression, Random Forest Regressor, and Gradient Boosting Regressor using MAE, RMSE, and $R^2$ score.
- **Residual Diagnostics:** Plotted residuals against fitted values to confirm that error terms are homoscedastic and normally distributed around zero.

### 🏆 Results
- **Champion Model:** **Gradient Boosting Regressor** achieved an $R^2$ score of **95.39%** with a Mean Absolute Error (MAE) of just **₹0.44 Lakhs**, accurately capturing non-linear automotive depreciation curves. Showroom price and car age accounted for over 85% of price variance.

---

## 🛡️ Project 4: Email Spam Detection with NLP & Machine Learning

**Objective:** Design, build, and evaluate a Natural Language Processing (NLP) binary classification pipeline capable of classifying emails and SMS messages into legitimate (*ham*) or *spam*.

### 🔍 Methodology & Pipeline
- **Text Cleansing:** Implemented regex routines to strip URLs, special characters, and digits, converted text to lowercase, removed NLTK English stopwords, and applied Porter Stemming.
- **Feature Extraction:** Transformed cleaned text into numerical vector spaces using **TF-IDF (Term Frequency-Inverse Document Frequency)** with unigram and bigram tokenization ($N=2,500$ features).
- **Lexical Exploration:** Generated WordClouds showing prominent keyword clusters in spam messages (e.g., *free, win, cash, urgent, call, prize*) versus ham messages.

### 🏆 Results & Precision Trade-off
- **Evaluation:** Evaluated Multinomial Naive Bayes, Linear Support Vector Classifier, Random Forest, and Logistic Regression.
- **Outcome:** **Multinomial Naive Bayes** achieved **100.00% Accuracy and 1.00 Precision**.
- **Critical Takeaway:** In spam detection, **Precision is paramount**. A False Positive (classifying a critical business or personal email as spam) is catastrophic, whereas a False Negative (letting a promotional spam email slip into the inbox) is a minor inconvenience.

---

## 📊 Project 5: Sales Prediction Using Python (Marketing Attribution)

**Objective:** Build a multivariate regression model to forecast product sales volumes based on advertising budget allocations across Television, Radio, and Newspaper channels.

### 🔍 Methodology & Budget Allocation Insights
- **EDA & Linearity:** Visualized channel spend vs. sales volume relationships with linear regression trendlines.
- **Models Benchmarked:** Compared Linear Regression, Polynomial Regression (Degree 2), and Random Forest Regressor.
- **Channel Attribution Analysis:**
  - **Radio:** Yielded the highest marginal return per dollar invested ($+0.181$ sales units per $1,000 spend).
  - **Television:** Consistently drove high baseline brand reach ($+0.045$ units per $1,000 spend).
  - **Newspaper:** Displayed negligible statistical significance ($p > 0.05$), indicating marketing budgets should be shifted from print toward digital and audio broadcast channels.

---

## 💡 Key Learnings & Takeaways

1. **EDA is 80% of Data Science:** Thorough exploratory analysis reveals feature distributions, multicollinearity, and data quality issues long before model training begins.
2. **Evaluation Beyond Accuracy:** For imbalanced classification tasks (like Spam Detection) or regression problems (like Car Valuation), metrics such as Precision, Recall, MAE, and $R^2$ provide crucial business context that simple accuracy hides.
3. **End-to-End Workflow:** Documenting code, persisting datasets, providing reproducible notebooks, and explaining analytical decisions is what turns code into real engineering.

---

## 🙏 Acknowledgements

I want to extend my sincere gratitude to **[Oasis Infobyte](https://oasisinfobyte.com/)** for designing such a practical, project-based internship curriculum. The tasks challenged me to apply machine learning concepts to real-world datasets and helped me build confidence in end-to-end data science workflows.

Feel free to check out my repository and connect with me:
- **GitHub Repository:** [github.com/pawaraditya0903/OIBSIP](https://github.com/pawaraditya0903/OIBSIP)
- **LinkedIn:** [Connect with Aditya](https://www.linkedin.com)

*Tags: #DataScience #MachineLearning #Python #OasisInfobyte #Internship #ArtificialIntelligence #NLP*
