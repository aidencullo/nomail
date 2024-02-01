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
    return parser.parse(date_str)


def format_subject(subject_str):
    subject = decode_header(subject_str)[0][0]
    if isinstance(subject, bytes):
        subject = decode_bytes(subject)
    return subject


def decode_bytes(subject):
    try:
        return subject.decode()
    except UnicodeDecodeError:
        return subject.decode('unicode_escape')

    
def format_uid(uid_str):
    return int(uid_str)
