from download_history import download_history
from calculate_rsi import calculate_rsi, compute_rsi
from rsi_same_day_df import rsi_same_day_df

df = download_history("ITUB4.SA")
print(df)

calculate_rsi("ITUB4.SA")

rsi = compute_rsi(df['Close'], period=14)
print(rsi.tail(10))

last_rsi = rsi.iloc[-1]
print(f"Last RSI value: {last_rsi}")

signal = rsi_same_day_df(
    tickers = ["ITUB4.SA", "AAPL", "VALE3.SA", "ABEV3.SA", "BBDC4.SA"],
    buy_below = 30,
    sell_above = 70,
    rsi_period = 14,
    start = '2026-01-01',
    auto_adjust = True,
    multi_level_index = False
)
print(signal)
