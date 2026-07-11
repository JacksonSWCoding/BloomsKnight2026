import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from backend import run_stress_test

st.set_page_config(page_title="Macro-Shock Portfolio Stress Tester", layout="wide")

st.title("💰 Quantitative Portfolio Risk Analytics Engine")
st.subheader("Bloomberg FinTech Challenge Submission")
st.write("Upload portfolio to simulate immediate catastrophic drawdowns against major historical macroeconomic shocks.")

st.sidebar.header("📁 Upload Portfolio")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file (Columns: Ticker, Shares)", type=["csv"])

st.sidebar.markdown("""
**Expected CSV Format:**

(Example)
Ticker,Shares
NVDA,5
TSLA,5
MSFT,5
""")

if uploaded_file is not None:
    try:
        portfolio_df = pd.read_csv(uploaded_file)

        if 'Ticker' not in portfolio_df.columns or 'Shares' not in portfolio_df.columns:
            st.error("Error: CSV must contain exactly 'Ticker' and 'Shares' columns.")
        else:
            st.success("Portfolio successfully loaded!")

            with st.spinner("Fetching historical market data and calculating risk metrics..."):
                results, total_value = run_stress_test(portfolio_df)

            # --- 8. Portfolio Statistics ---
            st.markdown("### 📊 Portfolio Statistics")
            stat_cols = st.columns(5)

            # Calculate metrics
            num_holdings = len(portfolio_df)
            max_pos_row = portfolio_df.loc[portfolio_df['Total Value'].idxmax()]
            min_pos_row = portfolio_df.loc[portfolio_df['Total Value'].idxmin()]
            avg_size = total_value / num_holdings if num_holdings > 0 else 0

            with stat_cols[0]:
                st.metric(label="Holdings", value=f"{num_holdings}")
            with stat_cols[1]:
                st.metric(label="Current Value", value=f"${total_value:,.2f}")
            with stat_cols[2]:
                st.metric(label="Largest Position",
                          value=f"{max_pos_row['Ticker']} (${max_pos_row['Total Value']:,.2f})")
            with stat_cols[3]:
                st.metric(label="Smallest Position",
                          value=f"{min_pos_row['Ticker']} (${min_pos_row['Total Value']:,.2f})")

            st.markdown("---")
            st.markdown("### Current Asset Allocation")

            colors = sns.color_palette("pastel")[0:len(portfolio_df)]

            chart_col, blank_col = st.columns([3, 7])

            with chart_col:
                fig_pie, ax_pie = plt.subplots(figsize=(3.5, 2.2))
                ax_pie.pie(
                    portfolio_df['Total Value'],
                    labels=portfolio_df['Ticker'],
                    autopct='%1.1f%%',
                    startangle=140,
                    colors=colors,
                    textprops={'fontsize': 7}
                )
                ax_pie.axis('equal')
                st.pyplot(fig_pie)

            st.markdown("---")

            # --- 5. Timeline Implementation ---
            st.markdown("### Historical Scenarios Timeline")

            # Custom styled CSS timeline line (Fixed parameter name here)
            st.markdown(
                """
                <div style="display: flex; justify-content: space-between; items-align: center; margin-bottom: 25px; padding: 20px; background-color: #1E222D; border-radius: 8px; border-left: 10px solid #31363F;">
    <div style="text-align: center; flex: 1;">
        <strong style="color: #FF4B4B; font-size: 42px;">2000</strong><br>
        <span style="font-size: 26px; color: #B2B5BE;">● Dot-Com</span>
    </div>
    <div style="text-align: center; flex: 1;">
        <strong style="color: #FF4B4B; font-size: 42px;">2008</strong><br>
        <span style="font-size: 26px; color: #B2B5BE;">● Financial Crisis</span>
    </div>
    <div style="text-align: center; flex: 1;">
        <strong style="color: #FF4B4B; font-size: 42px;">2018</strong><br>
        <span style="font-size: 26px; color: #B2B5BE;">● Rate Hike</span>
    </div>
    <div style="text-align: center; flex: 1;">
        <strong style="color: #FF4B4B; font-size: 42px;">2020</strong><br>
        <span style="font-size: 26px; color: #B2B5BE;">● COVID</span>
    </div>
    <div style="text-align: center; flex: 1;">
        <strong style="color: #FF4B4B; font-size: 42px;">2022</strong><br>
        <span style="font-size: 26px; color: #B2B5BE;">● Inflation</span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### ⚠ Simulated Shock Results")
            cols = st.columns(len(results))

            shock_names = []
            losses_pct = []

            # Mapping keys to account for backend dictionary formatting
            crisis_details = {
                "Dot-Com Bubble": {
                    "cause": "Speculative tech equity bubble burst.",
                    "duration": "March 2000 - October 2002",
                    "sectors": "Technology, Telecommunications, Internet IPOs"
                },
                "2008 Financial Crisis": {
                    "cause": "Subprime mortgage meltdown and structural credit freeze.",
                    "duration": "October 2007 - March 2009",
                    "sectors": "Financials, Real Estate, Investment Banking"
                },
                "2018 Fed Rate Hike Selloff": {
                    "cause": "Aggressive quantitative tightening and slowing global data.",
                    "duration": "September 2018 - December 2018",
                    "sectors": "Growth Equities, Technology, Small-Caps"
                },
                "2020 COVID Crash": {
                    "cause": "Sudden economic halts driven by pandemic lockdowns.",
                    "duration": "February 2020 - March 2020",
                    "sectors": "Hospitality, Energy, Aviation, Cruise Lines"
                },
                "2022 Inflation & Rate Shock": {
                    "cause": "Post-pandemic inflation spikes matched by sharp Fed interest rate hikes.",
                    "duration": "January 2022 - October 2022",
                    "sectors": "Tech, Long-duration growth assets, Fixed Income"
                }
            }

            for i, (scenario, metrics) in enumerate(results.items()):
                # Extract clean core name to fetch descriptions safely
                core_name = scenario.split("\n\n")[0]
                details = crisis_details.get(core_name,
                                             {"cause": "Historical macroeconomic shock scenario.", "duration": "N/A",
                                              "sectors": "N/A"})

                shock_names.append(core_name)
                losses_pct.append(metrics['loss_percentage'])

                with cols[i]:
                    # --- 6. Expandable Cards ---
                    with st.expander(f" {core_name}", expanded=True):
                        is_loss = metrics['dollar_loss'] < 0
                        label_text = "Projected Loss" if is_loss else "Projected Gain"
                        value_text = f"-${abs(metrics['dollar_loss']):,.2f}" if is_loss else f"+${metrics['dollar_loss']:,.2f}"

                        st.metric(
                            label=label_text,
                            value=value_text,
                            delta=f"{metrics['loss_percentage']:.2f}%"
                        )

                        st.markdown(f"**Cause:** {details['cause']}")
                        st.markdown(f"**Duration:** {details['duration']}")
                        st.markdown(f"**Remaining Value:** ${metrics['remaining_value']:,.2f}")
                        st.markdown(f"**Key Sectors Affected:** {details['sectors']}")

            st.markdown("---")
            st.markdown("### Historical Comparison")

            # --- Charting section with optimized font sizes ---
            sns.set_theme(style="darkgrid")
            fig, ax = plt.subplots(figsize=(10, 5))

            bar_colors = ['#d9534f' if x < 0 else '#5cb85c' for x in losses_pct]

            sns.barplot(x=shock_names, y=losses_pct, palette=bar_colors, ax=ax)
            ax.set_ylabel("Projected Value Change (%)", fontsize=10)
            ax.set_title("Portfolio Performance & Drawdown Severity Comparison", fontsize=12)

            ax.tick_params(axis='x', labelsize=8)
            ax.tick_params(axis='y', labelsize=9)

            ax.axhline(0, color='black', linewidth=1, linestyle='--')

            for p in ax.patches:
                height = p.get_height()
                va_dir = 'bottom' if height >= 0 else 'top'
                xy_off = (0, 5) if height >= 0 else (0, -12)

                ax.annotate(f"{height:.2f}%", (p.get_x() + p.get_width() / 2., height),
                            ha='center', va=va_dir, xytext=xy_off, textcoords='offset points', fontsize=8)

            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred while processing the data: {e}")
else:
    st.info("Please upload a portfolio CSV file in the sidebar to begin the stress analysis.")
