import pandas as pd
import yfinance as yf


def get_ticker_info(ticker_symbol: str) -> pd.DataFrame:
    """
    Get the ticker information from Yahoo Finance.

    Args:
        ticker_symbol (str): The ticker symbol.
    """

    ticker_obj = yf.Ticker(ticker_symbol)
    info = ticker_obj.info
    cashflow = ticker_obj.cashflow
    
    campos = [
        'returnOnEquity', # ROE: quanto lucro a empresa gera sobre o patrimônio líquido
        'returnOnAssets', # ROA: quanto lucro a empresa gera sobre os ativos que ela tem
        'totalDebt', # dívida total: quanto a empresa deve de dívidas
        'marketCap', # valor de mercado: quanto a empresa vale no mercado
        'priceToBook', # preço sobre valor patrimonial (P/VP): compara o preço da ação com o valor contábil por ação
        'totalCash', # caixa total: quanto de dinheiro/equivalentes a empresa tem disponível
        'operatingCashflow', # fluxo de caixa operacional: dinheiro que entra de verdade das operações do negócio
        'dividendYield', # quanto a empresa paga de dividendo por ano em relação ao preço da ação
        'payoutRatio', # qual % do lucro a empresa distribui como dividendo
        'profitMargins', # margem líquida: quanto sobra de lucro líquido para cada real de receita
        'operatingMargins', # margem operacional: quanto sobra de lucro operacional (antes de juros/impostos) para cada real de receita
        'totalRevenue', # receita total: quanto a empresa faturou no período
        'netIncomeToCommon', # lucro líquido disponível aos acionistas ordinários
    ]

    dados = {campo: info.get(campo) for campo in campos}
    df = pd.DataFrame([dados])

    # Calculate ROIC (Return on Invested Capital)
    df['roic'] = df['netIncomeToCommon'] / (df['totalDebt'] + df['marketCap'] - df['totalCash'])

    # Calculate Debt/Equity ratio
    df['debt/equity'] = df['totalDebt'] / (df['marketCap'] / df['priceToBook'])

    # Calculate FCF (Free Cash Flow)
    fcf = cashflow.loc['Free Cash Flow'][0]
    df['fcf'] = fcf

    return df
