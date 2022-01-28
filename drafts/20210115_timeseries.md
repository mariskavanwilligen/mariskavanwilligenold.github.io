Title: Timeseries
Date: 2021-01-14 15:20
Modified: 2021-01-14 15:20
Tags: Timeseries, Intro, Trend, Noise, Seasonality
Slug: timeseries
Authors: Mariska van Willigen
Summary: Introduction to timeseries

## Introduction of Time Series forecasting

## Components of Time Series
Time series analysis provides a body of techniques to better understand a dataset.
Perhaps the most useful of these is the decomposition of a time series into 4 constituent parts:

- **Level**:  The baseline value for the series if it were a straight line.
- **Trend**: The optional and often linear increasing or decreasing behavior of the series over time.
- **Seasonality**: The optional repeating patterns or cycles of behavior over time.
- **Noise**: The optional variability in the observations that cannot be explained by the model.

```js
y = level + trend + seasonality + noise
```
## Decomposition

## Multivariate Time Series vs Univariate Time Series

## Overview of some Time Series Forecasting models
- Autoregression (AR)
- Moving Average (MA)
- Autoregressive Moving Average (ARMA)
- Autoregressive Integrated Moving Average (ARIMA)
- Seasonal Autoregressive Integrated Moving-Average (SARIMA)
- Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX)
- Vector Autoregression (VAR)
- Vector Autoregression Moving-Average (VARMA)
- Vector Autoregression Moving-Average with Exogenous Regressors (VARMAX)
- Simple Exponential Smoothing (SES)
- Holt Winter’s Exponential Smoothing (HWES)