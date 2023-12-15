import pandas as pd

def write_csv(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv(file_name)

def read_csv(file_name):
    df = pd.read_csv(file_name, index_col=0)
    return [address.item() for address in df.values]
