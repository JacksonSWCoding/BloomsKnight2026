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
