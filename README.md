# Quantitative Portfolio Risk Analytics Engine
> **Bloomberg FinTech Challenge Submission**

An institutional-grade portfolio risk dashboard built to stress-test custom equity portfolios against major historical macroeconomic crises in real time.

---

## Overview
The **Quantitative Portfolio Risk Analytics Engine** allows investors to upload a custom CSV portfolio and instantly evaluate their downside exposure. Using live market data from `yfinance`, the engine calculates exact position weights and simulates how the portfolio would have performed during 5 catastrophic market shocks:
* **Dot-Com Bubble** (2000–2002)
* **2008 Financial Crisis** (2007–2009)
* **2018 Fed Rate Hike Selloff** (Sep–Dec 2018)
* **2020 COVID Crash** (Feb–Mar 2020)
* **2022 Inflation & Rate Shock** (Jan–Oct 2022)

---

## Key Features
* **CSV Portfolio Ingestion:** Parses uploaded tickers and share quantities to dynamically compute total portfolio value and position weightings.
* **Smart Cash-Proxy Fallback:** Automatically treats assets not yet publicly traded during historical shocks as cash (0% return impact) to ensure error-free calculations.
* **Interactive Macro Timeline:** Features a custom HTML/CSS historical timeline highlighting key market regimes.
* **Detailed Scenario Expander Cards:** Displays projected dollar losses, percentage drawdowns, remaining portfolio values, core triggers, and affected sectors per crisis.
* **Visual Drawdown Analytics:** Renders capital allocation pie charts and dynamic Seaborn drawdown comparison bar charts.

---

## Tech Stack & Tools
* **Language:** Python
* **Data Ingestion & Quantitative Logic:** `yfinance`, `pandas`, `numpy`
* **Frontend UI & Layout:** `streamlit`, HTML/CSS
* **Data Visualization:** `matplotlib`, `seaborn`

---

## Future Work
## 🔮 Future Work & Roadmap

### 1. Predictive Black-Swan Scenario Modeling
* **Custom Epidemic & Macro Stress Simulator:** Expand beyond historical backtesting by building a predictive factor model to simulate hypothetical black-swan events (e.g., severe global health outbreaks like Hantavirus, supply chain shocks, or geopolitical tensions).
* **Multi-Factor Sensitivity Engine:** Train regression models on historical market regimes using `scikit-learn` to estimate sector-specific shock elasticities ($\beta$) across mobility, volatility, and supply chain metrics.
* **Stochastic Monte Carlo Simulations:** Incorporate Geometric Brownian Motion (GBM) with custom shock drift parameters to generate probabilistic price distributions (5th–95th percentile drawdowns) over 30/60/90-day horizons.

### 2. Real-Time Data Pipeline & Streaming
* **Live Market Feeds:** Integrate streaming WebSocket connections via Alpha Vantage or Financial Modeling Prep APIs to calculate true real-time portfolio valuations and intraday VaR metrics.
* **Expanded Historical Repertoire:** Incorporate additional historical regimes.

### 3. AI-Driven Portfolio Optimization & Automated Hedging
* **Intelligent Risk Mitigation:** Leverage LLM (Large Language Model) integrations to analyze portfolio risk concentration and generate targeted, actionable hedging strategies (e.g., suggesting sector rotations or put option overlays to offset calculated Value at Risk).
* **Automated Rebalancing Engine:** Provide mean-variance optimization (Sharpe ratio maximization) to dynamically suggest optimal weight adjustments based on user risk tolerance.


---

## Try It Yourself!

### 1. PyCharm Setup
1. Download and install **PyCharm Community Edition** (free) or **Professional** from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/).
2. Open PyCharm, select **Open**, and navigate to your project folder.
3. Configure your Python Interpreter:
   * Navigate to **Settings/Preferences** > **Project** > **Python Interpreter**.
   * Click **Add Interpreter** > **Add Local Interpreter...** and create a new **Virtualenv**.

### 2. Install Dependencies
Open the PyCharm Terminal (`Alt + F12` or **View** > **Tool Windows** > **Terminal**) and run:

```bash
pip install pandas yfinance numpy streamlit matplotlib seaborn

* In the PyCharm Terminal, launch the Streamlit app:
  streamlit run app.py

Upload a .csv file formatiied with Ticker and Shares columns:
  Ticker,Shares
  NVDA,5
  TSLA,5
  MSFT,5
