import streamlit as st
from rsi_same_day_df import rsi_same_day_df

st.title("📊 Acompanhe seu portifólio - Tabela RSI")

tickers = ['CMIG4.SA', 'SAPR11.SA', 'BBAS3.SA']

df = rsi_same_day_df(
    tickers=tickers,
    buy_below=30,
    sell_above=70,
    rsi_period=14,
    start='2026-01-01',
    auto_adjust= True
)
    
st.dataframe(df, width="stretch")
