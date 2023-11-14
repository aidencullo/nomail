import pandas as pd
from datetime import datetime

def print_file(data=None):
    if data == None:
        data = []
    data = {
        'emails': data,
    }

    df = pd.DataFrame(data)

    # file_name = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
    file_name = datetime.today().isoformat()
    file_name = 'summaries/' + file_name + '.html'
    
    df.to_html(file_name)
