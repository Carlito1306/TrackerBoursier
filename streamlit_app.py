#!/usr/bin/env python3
import streamlit as st
import yfinance

TICKERS = sorted(["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "JPM", "V", "MA", "HD", "PG", "COST", "NFLX", "DIS", "PYPL", "SQ", "SHOP", "COIN", "AMD", "INTC", "BA", "CAT", "GS", "SBUX", "NKE", "F", "GM", "RIVN", "LCID", "NIO", "RY.TO", "TD.TO", "BMO.TO", "BNS.TO", "ENB.TO", "SHOP.TO", "BCE.TO", "SPY", "QQQ", "VOO", "VTI", "ARKK", "GLD", "XQQ.TO", "VFV.TO", "XEQT.TO", "BTC-USD", "ETH-USD", "SOL-USD", "DOGE-USD"])

st.set_page_config(page_title="Tracker Boursier", page_icon="📈")
st.title("📈 Tracker Boursier Instantané")

symbole = st.selectbox("Sélectionnez un symbole :", [""] + TICKERS)

if symbole:
    ticker = yfinance.Ticker(symbole)
    data = ticker.history(period="2d")
    if len(data) >= 2:
        prix = data["Close"].iloc[-1]
        var = prix - data["Close"].iloc[-2]
        pct = (var / data["Close"].iloc[-2]) * 100
        st.metric(f"{symbole}", f"${prix:.2f}", f"{var:+.2f}$ ({pct:+.2f}%)")
        st.subheader("📊 Historique")
        p = st.selectbox("Période", ["1mo","3mo","6mo","1y","5y"], format_func=lambda x: {"1mo":"1 mois","3mo":"3 mois","6mo":"6 mois","1y":"1 an","5y":"5 ans"}[x])
        st.line_chart(ticker.history(period=p)["Close"])
