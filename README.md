
A beginner-friendly Python investing algorithm that uses moving averages to generate buy and hold signals, then backtests the strategy against the market.

## Overview

This project downloads historical stock data, calculates two moving averages, and uses them to decide when to be in or out of the market.

The core idea is simple:

- Buy when the short-term moving average is above the long-term moving average
- Stay out of the market when it is not
- Compare the strategy's performance against buy-and-hold

This project is useful for learning:

- Python for finance
- pandas DataFrames
- trading signals
- backtesting basics
- strategy evaluation

## Strategy Logic

The algorithm uses:

- A **short moving average** (example: 20 days)
- A **long moving average** (example: 50 days)

### Buy Rule
Enter or hold a position when:

short moving average > long moving average

### Exit Rule
Exit or stay out when:

short moving average <= long moving average

## Features

- Downloads historical price data with `yfinance`
- Stores data in a pandas DataFrame
- Calculates moving averages
- Generates trading signals
- Computes market returns
- Computes strategy returns
- Tracks cumulative growth
- Calculates win rate
- Compares strategy performance to the market

## Project Structure

```bash
project-folder/
│
├── investing_algorithm.py
├── README.md
└── requirements.txt

## Activation of Enviorment & Libraries
- python3 -m venv (virtual enviornment name)
- source (virtual environment name)/bin/activate  (linux)
- pip install -r requirements.txt
- python3 main.py# Lucky-no.7 
