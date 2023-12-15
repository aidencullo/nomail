import re
from datetime import datetime
from email.header import decode_header

def format_email(msg):
    raw_email = msg["From"]
    for item in raw_email.split():
        if '@' in item:
            email = item
    email = re.sub('[<>]',"", email)
    return email

def format_date(msg):
    date_str = msg["Date"]
    date_str = re.sub('\(.*\)',"", date_str)
    date_str = re.sub('GMT',"", date_str)
    date_str = re.sub('UTC',"", date_str)
    date_str = date_str.strip()

    date_format_1 = "%d %b %Y %H:%M:%S %z"
    date_format_2 = "%a, %d %b %Y %H:%M:%S %z"
    date_format_3 = "%a, %d %b %Y %H:%M:%S"

    from pytz import timezone

    for fmt in (date_format_1, date_format_2, date_format_3):
        try:
            dt = datetime.strptime(date_str, fmt)
            dt = dt.astimezone()
            dt = dt.replace(tzinfo=None)
            return dt
        except ValueError:
            pass
    raise ValueError('no valid date format found')

def format_subject(msg):
    subject = decode_header(msg["Subject"])
    text_fragments = []
    for data, data_type in subject:
        try:
            text_fragments.append(data.decode())
        except (UnicodeDecodeError, AttributeError):
            text_fragments.append(data)
    subject = ' '.join(text_fragments)
    return subject

def format_data(msg):    
    return {
        'subject': format_subject(msg), 
        'from': format_email(msg),
       'date': format_date(msg),
    }