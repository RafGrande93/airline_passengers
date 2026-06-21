# Air Passengers Forecasting with Time Series Analysis

This project analyzes monthly airline passenger numbers from 1949 to 1960 using time series analysis techniques. The goal is to identify trend and seasonality patterns in the data and compare different forecasting models.

## Project Overview

The notebook performs the following steps:

1. Loads and cleans the airline passenger dataset
2. Converts monthly date values into a proper datetime format
3. Performs exploratory data analysis
4. Checks for trend, seasonality, autocorrelation, and stationarity
5. Applies differencing to make the series stationary
6. Builds and compares forecasting models
7. Evaluates model performance using MAE and R²

## Dataset

The dataset contains monthly airline passenger counts. The columns represent the month and the number of passengers.

The dataset includes 144 monthly observations from 1949 to 1960.

## Methods Used

The project compares three forecasting approaches:

### Seasonal Naive Forecast

A simple baseline model that repeats passenger values from the same month in the previous year.

### Prophet

A forecasting model designed for time series data with trend and seasonality.

### SARIMA

A Seasonal ARIMA model used to capture both trend and yearly seasonal patterns in the passenger data.

## Results

The models were evaluated using MAE and R². SARIMA was the best-performing model, with an R² score of 0.80, followed by Prophet with an R² score of 0.72. The seasonal naive model served as the baseline with an R² score of 0.07.

## Requirements

The project uses the following Python libraries:

* NumPy
* pandas
* Matplotlib
* scikit-learn
* statsmodels
* Prophet
