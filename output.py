import pandas as pd

def print_file(data=None, file_name='data.html'):
    if data == None:
        data = []
    data = {
        'emails': data,
    }

    df = pd.DataFrame(data)
    df.to_html(file_name)
