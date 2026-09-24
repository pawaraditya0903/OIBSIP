# 🎥 Oasis Infobyte SIP — Demo Video Walkthrough Scripts

This guide provides the exact spoken script and timing for recording your 1-to-2 minute demo walkthrough videos.

---

## ⚠️ Mandatory Video Format Rule
Every video **MUST** begin with a **2-second static title card or text overlay** showing:
1. **Full Name:** Aditya
2. **Assigned Track:** Data Science
3. **Task Title:** (e.g., *Task 1: Iris Flower Classification*)

> 💡 **Quick Tool:** Double-click [`title_card_generator.html`](title_card_generator.html) in your browser, select your task, click "Fullscreen", and let it display on your recording for the first 3 seconds before switching windows!

---

## 🎙️ Script 1: Task 1 — Iris Flower Classification (Duration: ~1.5 mins)

### [0:00 - 0:03] Title Card Screen
*(Show the Title Card on full screen for 3 seconds)*
> **Text displayed:**  
> **Name:** Aditya  
> **Track:** Data Science  
> **Task 1:** Iris Flower Classification  
> **Oasis Infobyte SIP**

### [0:03 - 0:30] Introduction & Dataset Walkthrough
*(Switch screen to your Jupyter Notebook or VS Code)*
> "Hello everyone! My name is Aditya, and in this video, I will be presenting my Task 1 project for the Oasis Infobyte Data Science Internship: Iris Flower Classification.  
> The goal of this task is to train and compare supervised classification algorithms to predict iris flower species based on four physical measurements: Sepal Length, Sepal Width, Petal Length, and Petal Width.  
> We began by performing Exploratory Data Analysis, verifying data integrity with zero missing values, and generating a pairplot and boxplots."

### [0:30 - 1:00] Visualizations & Feature Importance
*(Scroll to the Pairplot and Boxplot charts)*
> "As seen in the pairplot and boxplots, Petal Length and Petal Width are the most discriminative features. Iris Setosa is completely linearly separable from the other two species with petal lengths under 2 centimeters.  
> We applied standard scaling to normalize feature magnitudes and split our data into an 80% training set and 20% test set using stratified sampling."

### [1:00 - 1:30] Models & Results
*(Scroll to the Model Comparison bar chart and Confusion Matrix)*
> "We trained 5 candidate classifiers: Logistic Regression, K-Nearest Neighbors, Decision Trees, Random Forest, and Support Vector Machine.  
> On our unseen test dataset, our Linear Support Vector Classifier achieved a flawless 100% accuracy, while Random Forest and Logistic Regression achieved 96.67% accuracy.  
> Thank you to Oasis Infobyte for this wonderful learning opportunity!"

---

## 🎙️ Script 2: Task 2 — Unemployment Analysis with Python (Duration: ~1.5 mins)

### [0:00 - 0:03] Title Card Screen
> **Name:** Aditya | **Track:** Data Science | **Task 2:** Unemployment Analysis in India

### [0:03 - 0:30] Problem Context & Data
> "Hello everyone! This is Aditya presenting Task 2 for the Oasis Infobyte Data Science Internship: Unemployment Analysis with Python.  
> In this project, we performed extensive exploratory data analysis on the Indian unemployment trajectory from May 2019 to October 2020, focusing on the acute economic impact caused by the COVID-19 pandemic and national lockdown."

### [0:30 - 1:00] Trends & Lockdown Impact
*(Show the Time-Series chart and Top 10 States bar chart)*
> "Looking at our time-series line chart, we clearly observe a sharp, unprecedented spike in unemployment in April and May 2020 following the nationwide lockdown, surging from an average baseline of 9.2% up to over 28% in heavily affected industrial zones.  
> Our regional analysis identifies states like Haryana, Tripura, and Bihar experiencing the highest sustained unemployment rates during this period."

### [1:00 - 1:30] Correlation & Conclusion
*(Show the Correlation Heatmap and Pre vs Post COVID boxplot)*
> "The correlation matrix confirms an inverse relationship between unemployment rate and labor participation rate, highlighting the discouraged worker effect during peak restrictions.  
> In summary, this EDA demonstrates the resilience of different geographic zones and provides clear data-driven takeaways for economic recovery policies. Thank you Oasis Infobyte!"

---

## 🎙️ Script 3: Task 3 — Car Price Prediction (Duration: ~1.5 mins)

### [0:00 - 0:03] Title Card Screen
> **Name:** Aditya | **Track:** Data Science | **Task 3:** Car Price Prediction with Machine Learning

### [0:03 - 0:30] Objective & Feature Engineering
> "Hello everyone! I am Aditya, presenting Task 3: Car Price Prediction for Oasis Infobyte.  
> Our objective is to predict the resale price of used cars using features such as vehicle age, showroom price, kilometers driven, fuel type, transmission, and seller channels.  
> We engineered a vehicle age feature from the manufacturing year and performed one-hot encoding on categorical variables."

### [0:30 - 1:15] Modeling & Evaluation
*(Show the Price vs Age regression plot, Feature Importance, and Model Comparison)*
> "We benchmarked four regression models: Linear Regression, Ridge Regression, Random Forest, and Gradient Boosting.  
> Our Gradient Boosting Regressor performed the best, achieving an impressive R-squared score of 95.39% with a Mean Absolute Error of just 0.44 Lakhs.  
> Feature importance analysis reveals that original showroom price and vehicle age contribute over 85% to used car resale valuations. Thank you Oasis Infobyte!"

---

## 🎙️ Script 4: Task 4 — Email Spam Detection (Duration: ~1.5 mins)

### [0:00 - 0:03] Title Card Screen
> **Name:** Aditya | **Track:** Data Science | **Task 4:** Email Spam Detection with Machine Learning

### [0:03 - 0:30] NLP Pipeline & TF-IDF
> "Hello! I am Aditya, presenting Task 4: Email Spam Detection using Machine Learning.  
> In this NLP task, we built an end-to-end binary classification pipeline. We cleaned text data by stripping URLs, numbers, and punctuation, removing English stopwords, and applying Porter Stemming.  
> We converted messages into numerical features using TF-IDF Vectorization with unigrams and bigrams."

### [0:30 - 1:15] WordClouds & Precision Discussion
*(Show WordClouds and Confusion Matrices)*
> "WordCloud analysis reveals that spam messages heavily cluster around promotional words like 'free', 'win', 'urgent', 'cash', and 'prize', whereas legitimate ham messages feature everyday conversational terms.  
> We trained Multinomial Naive Bayes, Linear Support Vector Classifier, and Random Forest. Our Naive Bayes model achieved 100% accuracy and 100% precision. High precision is crucial in spam filtering to prevent critical business emails from being falsely quarantined as spam. Thank you Oasis Infobyte!"

---

## 🎙️ Script 5: Task 5 — Sales Prediction Using Python (Duration: ~1.5 mins)

### [0:00 - 0:03] Title Card Screen
> **Name:** Aditya | **Track:** Data Science | **Task 5:** Sales Prediction Using Python

### [0:03 - 1:15] Marketing Spend Attribution
> "Hello everyone, my name is Aditya and this is Task 5: Sales Prediction Using Python for the Oasis Infobyte Data Science Internship.  
> We analyzed the impact of advertising spend across Television, Radio, and Newspaper channels on product sales.  
> We evaluated Linear Regression, Polynomial Regression, and Random Forest. Random Forest achieved the highest R-squared score of 94.88%.  
> Examining our regression coefficients, Radio spend yielded the highest marginal sales impact per dollar invested, followed closely by TV advertising, while Newspaper spend showed negligible statistical impact. Thank you Oasis Infobyte!"
