import re
from datetime import datetime

def format_email(raw_email):
    for item in raw_email.split():
        if '@' in item:
            email = item
    email = re.sub('[<>]',"", email)
    return email

def format_date(date_str):
    date_str = re.sub('\(.*\)',"", date_str)
    date_str = re.sub('GMT',"", date_str)
    date_str = re.sub('UTC',"", date_str)
    date_str = date_str.strip()
    
    date_format_1 = "%d %b %Y %H:%M:%S %z"
    date_format_2 = "%a, %d %b %Y %H:%M:%S %z"
    date_format_3 = "%a, %d %b %Y %H:%M:%S"

    for fmt in (date_format_1, date_format_2, date_format_3):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    print(date_str)
    raise ValueError('no valid date format found')

def format_subject(subject):
    words = []
    for word in subject.split(' '):
        if 'UTF-8' not in word:
            words.append(word)
    subject = ' '.join(words)
    return subject
