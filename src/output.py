from datetime import datetime
import re
import pandas as pd

from src import email

def generate_file_name():
    return 'logs/' + re.sub('[ ]', '_', str(datetime.today())) + '.csv'

def write_emails_to_file(emails: email.EmailList) -> None:
    write_df_to_file(emails.to_df())

def write_df_to_file(df: pd.DataFrame) -> None:
    df.to_csv(generate_file_name(), index=False)
