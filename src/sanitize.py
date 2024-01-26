import re
from datetime import datetime
from email.header import decode_header

import pytz

def format_email(raw_email):
    if raw_email is None:
        return None
    for item in raw_email.split():
        if '@' in item:
            email = item
    email = re.sub('[<>]', "", email)
    return email


def format_date(date_str):
    date_str = re.sub('\(.*\)', "", date_str)
    date_str = re.sub('GMT', "", date_str)
    date_str = re.sub('UTC', "", date_str)
    date_str = date_str.strip()

    date_format_1 = "%d %b %Y %H:%M:%S %z"
    date_format_2 = "%a, %d %b %Y %H:%M:%S %z"
    date_format_3 = "%a, %d %b %Y %H:%M:%S"


    for fmt in (date_format_1, date_format_2, date_format_3):
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt
        except ValueError:
            pass
    raise ValueError('no valid date format found')


def format_subject(subject_str):
    subject = decode_header(subject_str)
    text_fragments = []
    for data, data_type in subject:
        try:
            text_fragments.append(data.decode())
        except (UnicodeDecodeError, AttributeError):
            text_fragments.append(data)
    subject = ' '.join(text_fragments)
    return subject


def format_uid(uid_str):
    return int(uid_str)
