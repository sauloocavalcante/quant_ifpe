import streamlit as st
from rsi_same_day_df import rsi_same_day_df
from backtest import ma_strategy

tab1, tab2 = st.tabs([
    'RSI', 'MA Strategy'
])

with tab1:
    st.title("📊 Acompanhe seu portifólio - Tabela RSI")

    tickers = ['CMIG4.SA', 'BBAS3.SA']

    df = rsi_same_day_df(
        tickers=tickers,
        buy_below=30,
        sell_above=70,
        rsi_period=14,
        start='2026-01-01',
        auto_adjust= True
    )
        
    st.dataframe(df, width="stretch")

with tab2:

    ticker = st.sidebar.text_input(
        'Choose your ticker:',
        value='BBAS3.SA'
    )
    ma_short_button = st.sidebar.number_input(
        'MA_short',
        min_value=1,
        max_value=100,
        value=9,
        step=1
    )

    ma_long_button = st.sidebar.number_input(
        'MA_short',
        min_value=50,
        max_value=300,
        value=72,
        step=1
    )
    df = ma_strategy(
            ticker=ticker, 
            ma_short=ma_short_button, 
            ma_long=ma_long_button
        )
    st.title(f'Strategy for: {ticker}')
    st.dataframe(df, width="stretch")
