from datetime import datetime
from pathlib import Path

import pandas as pd


def create_file_name():
    date = datetime.today()
    file_dir_array = ['summaries', date.year, date.month, date.day]
    file_dir = '/'.join(str(x) for x in file_dir_array)
    file_name_array = [date.time(), '.html']
    file_name = '/'.join((file_dir, ''.join(str(x) for x in file_name_array)))
    Path(file_dir).mkdir(parents=True, exist_ok=True)
    return file_name


def format_data(raw_data):
    raw_data = list(raw_data)
    data = {}
    for key in ['subject', 'from', 'date']:
        data[key] = [raw_unit[key] for raw_unit in raw_data]
    return data


def print_file(raw_data, file_name=None):
    data = format_data(raw_data)
    if file_name is None:
        file_name = create_file_name()
    data_frame = pd.DataFrame(data)
    data_frame.to_html(file_name, index=False)
