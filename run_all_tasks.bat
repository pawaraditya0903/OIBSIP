@echo off
echo ====================================================================
echo        OASIS INFOBYTE SIP - EXECUTING ALL 5 DATA SCIENCE TASKS
echo ====================================================================

echo.
echo [1/5] Running Task 1: Iris Flower Classification...
python DataScience-Task1-IrisFlowerClassification\iris_classification.py
if %errorlevel% neq 0 (
    echo [ERROR] Task 1 failed!
)

echo.
echo [2/5] Running Task 2: Unemployment Analysis with Python...
python DataScience-Task2-UnemploymentAnalysis\unemployment_analysis.py
if %errorlevel% neq 0 (
    echo [ERROR] Task 2 failed!
)

echo.
echo [3/5] Running Task 3: Car Price Prediction with Machine Learning...
python DataScience-Task3-CarPricePrediction\car_price_prediction.py
if %errorlevel% neq 0 (
    echo [ERROR] Task 3 failed!
)

echo.
echo [4/5] Running Task 4: Email Spam Detection with Machine Learning...
python DataScience-Task4-EmailSpamDetection\spam_detection.py
if %errorlevel% neq 0 (
    echo [ERROR] Task 4 failed!
)

echo.
echo [5/5] Running Task 5: Sales Prediction Using Python...
python DataScience-Task5-SalesPrediction\sales_prediction.py
if %errorlevel% neq 0 (
    echo [ERROR] Task 5 failed!
)

echo.
echo ====================================================================
echo   ALL 5 TASKS EXECUTED SUCCESSFULLY! YOUR SUBMISSION IS READY!
echo ====================================================================
pause
