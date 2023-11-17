import re
from datetime import datetime

def format_email(raw_email):
    for item in raw_email.split():
        if '@' in item:
            email = item
    email = re.sub('[<>]',"", email)
    return email

def format_date(date_str):
    date_format = "%a, %d %b %Y %H:%M:%S +0000 (UTC)"
    date_obj = datetime.strptime(date_str, date_format)
    return date_obj

def format_subject(subject):
    words = []
    for word in subject.split(' '):
        if 'UTF-8' not in word:
            words.append(word)
    subject = ' '.join(words)
    return subject
