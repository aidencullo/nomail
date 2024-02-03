from datetime import datetime
import re

import pandas as pd


def create_file_name():
    return re.sub('[-, ]','/', str(datetime.today())) + '.html'


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
