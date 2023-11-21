import pandas as pd
from datetime import datetime

def create_file_name():
    file_name = datetime.today().isoformat()
    file_name = 'summaries/' + file_name + '.html'
    return file_name

def format_data(raw_data):
    data = {}
    for key in ['subject', 'from', 'date']:
        data[key] = [raw_unit[key] for raw_unit in raw_data]
    return data

def print_file(raw_data, file_name):
    data = format_data(raw_data)
    # file_name = create_file_name()
    df = pd.DataFrame(data)
    df.to_html(file_name, index=False)
