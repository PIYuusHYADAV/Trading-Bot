# Binance Futures Testnet Trading Application

## Overview

A Python command-line application that interacts with the Binance Futures Testnet API to place futures orders. The project focuses on API integration, input validation, logging, and clean code organization.

## Features

- Place Market Orders
- Place Limit Orders
- Place Stop-Limit Orders
- Support BUY and SELL order sides
- Input validation for:
  - Symbol
  - Side
  - Order Type
  - Quantity
  - Price (when required)

- Request and response logging
- Error handling for invalid inputs, API errors, and network failures
- Clear order request and response output

## Project Structure

```text
PrimeTrade/
│
├── cli.py
│
└── bot/
    ├── client.py
    ├── orders.py
    ├── validators.py
    ├── config.py
    └── logging_config.py
```

## Components

### cli.py

Handles user input and displays order summaries and responses.

### validators.py

Validates user inputs before an API request is sent.

### orders.py

Contains order creation logic and request preparation.

### client.py

Handles communication with Binance Futures Testnet APIs.

### logging_config.py

Configures application logging and stores logs in a file.

### config.py

Stores application configuration and API credentials.

## Technologies Used

- Python 3
- Requests
- Binance Futures Testnet API
- Logging

## Example Usage

```bash
python cli.py
```

```text
Symbol: BTCUSDT
Side (BUY/SELL): BUY
Type (MARKET/LIMIT/STOP): MARKET
Quantity: 0.001
```

## Skills Demonstrated

- REST API Integration
- HMAC SHA256 Request Signing
- Input Validation
- Exception Handling
- Logging and Monitoring
- Modular Code Organization
- Basic Trading System Development

## Future Improvements

- OCO Order Support
- TWAP Orders
- Grid Trading Strategies
- Account Balance Display
- Position Management
- Automated Testing

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd PrimeTrade
```

### 2. Create a Virtual Environment

```bash
conda create -p venv python==3.10 -y
```

### 3. Activate the Virtual Environment

```bash
conda activate venv/
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Binance Futures Testnet Credentials

Create a `.env` file in the project root:

```env
API_KEY=your_api_key
SECRET_KEY=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

Replace the values with your Binance Futures Testnet API credentials.

### 6. Run the Application

```bash
python cli.py
```
