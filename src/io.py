import pandas as pd


def write_csv(data, file_name):
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(file_name)


def read_csv(file_name):
    data_frame = pd.read_csv(file_name, index_col=0)
    return [address.item() for address in data_frame.values]
