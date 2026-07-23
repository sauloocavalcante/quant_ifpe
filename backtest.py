import pandas as pd
import vectorbt as vbt

def ma_strategy(
        ticker:str,
        ma_short:int = 9,
        ma_long:int = 72,
        start_date:str = '2021-01-01'
) -> pd.DataFrame:

    price = (
        vbt.YFData.
            download('CPLE3.SA')
            .get('Close')
            .loc[start_date:]
    )

    mas = vbt.MA.run(price, window=ma_short)
    mal = vbt.MA.run(price, window=ma_long)

    entries = mas.ma_crossed_above(mal)
    exits = mas.ma_crossed_below(mal)

    portfolio=vbt.Portfolio.from_signals(
        close=price,
        entries=entries,
        exits=exits,
        init_cash=10_000,
        fees=0.0001,
        slippage=0.001
    )

    df = (
        portfolio
            .stats()
            .to_frame('Value')
    )

    return df