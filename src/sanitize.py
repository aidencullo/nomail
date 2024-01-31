from dateutil import parser
import re
from email.header import decode_header


def format_email(raw_email):
    if raw_email is None:
        return None
    for item in raw_email.split():
        if '@' in item:
            email = item
    email = re.sub('[<>]', "", email)
    return email


def format_date(date_str):
    parser.parse(date_str)
    # print(f'(\'{date_str}\',\'{date_datetime}\'),')
    return parser.parse(date_str)


def format_subject(subject_str):
    subject = decode_header(subject_str)
    text_fragments = []
    for data, _ in subject:
        try:
            text_fragments.append(data.decode())
        except (UnicodeDecodeError, AttributeError):
            if isinstance(data, bytes):
                data = data.decode('unicode_escape')
            text_fragments.append(data)
    subject = ' '.join(text_fragments)
    return subject


def format_uid(uid_str):
    return int(uid_str)
