from datetime import datetime
import re


def generate_file_name():
    return re.sub('[ ]','_', str(datetime.today())) + '.csv'

def write_to_file(df):
    df.to_csv(generate_file_name(), index=False)
