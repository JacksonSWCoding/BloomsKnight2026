import pandas as pd
import yfinance as yf
import numpy as np

def run_stress_test(portfolio_df):
    tickers = portfolio_df['Ticker'].tolist()

    # Fetch data going back to 1950
    data = yf.download(tickers, start="1950-01-01")['Close']

    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers[0])

    current_prices = data.iloc[-1]
    portfolio_df['Current Price'] = portfolio_df['Ticker'].map(current_prices)
    portfolio_df['Total Value'] = portfolio_df['Shares'] * portfolio_df['Current Price']

    total_portfolio_value = portfolio_df['Total Value'].sum()
    portfolio_df['Weight'] = portfolio_df['Total Value'] / total_portfolio_value

    shocks = {
        "2008 Financial Crisis\n\n (10/2007 - 3/2009)": ("2007-10-01", "2009-03-09"),
        "2020 COVID Crash\n\n (02/2020 - 03/2020)": ("2020-02-19", "2020-03-23"),
        "Dot-Com Bubble\n\n (3/2000 - 10/2002)": ("2000-03-10", "2002-10-09"),
        "2018 Fed Rate Hike Selloff\n\n (09/2018 - 12/2018)": ("2018-09-20", "2018-12-24"),
        "2022 Inflation & Rate Shock\n\n (01/2022 - 10/2022)": ("2022-01-03", "2022-10-12")
    }

    results = {}

    for name, (start_date, end_date) in shocks.items():
        scenario_data = data.loc[start_date:end_date]
        if scenario_data.empty:
            continue

        asset_drops = (scenario_data.iloc[-1] / scenario_data.iloc[0]) - 1
        portfolio_loss_pct = 0.0

        for _, row in portfolio_df.iterrows():
            ticker = row['Ticker']
            weight = row['Weight']

            # Check if the ticker has valid price data for this historical period
            if ticker in asset_drops and not pd.isna(asset_drops[ticker]):
                portfolio_loss_pct += asset_drops[ticker] * weight
            else:
                # If not publicly traded yet, it acts as cash (0% return impact)
                portfolio_loss_pct += 0.0 * weight

        results[name] = {
            "loss_percentage": portfolio_loss_pct * 100,
            "dollar_loss": total_portfolio_value * portfolio_loss_pct,
            "remaining_value": total_portfolio_value * (1 + portfolio_loss_pct)
        }

    return results, total_portfolio_value