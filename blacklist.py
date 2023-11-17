import pandas as pd

def get_blacklist():
    df = pd.read_csv('blacklist.csv', index_col=0)
    return [address.item() for address in df.values]
