import pandas as pd
from datetime import datetime

def create_file_name():
    file_name = datetime.today().isoformat()
    file_name = 'summaries/' + file_name + '.html'

def print_file(raw_data=None, file_name=None):
    if raw_data == None:
        raw_data = []

    data = {}
    keys = raw_data[0].keys()
    for key in keys:
        data[key] = [ raw_unit[key] for raw_unit in raw_data]

    # data = {
    #     'subject': [ raw_unit['subject'] for raw_unit in raw_data],
    #     'from': [ raw_unit['from'] for raw_unit in raw_data],
    #     'date': [ raw_unit['date'] for raw_unit in raw_data],
    # }

    df = pd.DataFrame(data)
    if file_name == None:
        file_name = create_file_name()    
    df.to_html(file_name)
