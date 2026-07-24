# BloomsKnight2026

Quantitative Portfolio Risk Analytics Engine
My Bloomberg FinTech Challenge Submission

An institutional-grade portfolio risk dashboard built to stress-test custom equity portfolios against major historical macroeconomic crises in real time.

----------------------

The Overview
The Quantitative Portfolio Risk Analytics Engine allows investors to upload a custom CSV portfolio and instantly evaluate their downside exposure. Using live market data from `yfinance`, the engine calculates exact position weights and simulates how the portfolio would have performed during 5 catastrophic market shocks:
1) Dot-Com Bubble (2000–2002)
2) 2008 Financial Crisis (2007–2009)
3) 2018 Fed Rate Hike Selloff (Sep–Dec 2018)
4) 2020 COVID Crash (Feb–Mar 2020)
5) 2022 Inflation & Rate Shock (Jan–Oct 2022)

----------------------

 Key Features
CSV Portfolio Ingestion: Parses uploaded tickers and share quantities to dynamically compute total portfolio value and position weightings.
* **Smart Cash-Proxy Fallback:** Automatically treats assets not yet publicly traded during historical shocks as cash (0% return impact) to ensure error-free calculations.
* **Interactive Macro Timeline:** Features a custom HTML/CSS historical timeline highlighting key market regimes.
* **Detailed Scenario Expander Cards:** Displays projected dollar losses, percentage drawdowns, remaining portfolio values, core triggers, and affected sectors per crisis.
* **Visual Drawdown Analytics:** Renders capital allocation pie charts and dynamic Seaborn drawdown comparison bar charts.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Ingestion & Quantitative Logic:** `yfinance`, `pandas`, `numpy`
* **Frontend UI & Layout:** `streamlit`, HTML/CSS
* **Data Visualization:** `matplotlib`, `seaborn`

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:

```bash
pip install pandas yfinance numpy streamlit matplotlib seaborn
