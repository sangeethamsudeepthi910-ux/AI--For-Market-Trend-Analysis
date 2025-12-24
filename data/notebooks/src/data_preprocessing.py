import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.month
    df['Year'] = df['Order Date'].dt.year
    return df
