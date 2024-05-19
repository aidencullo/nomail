import re
from email.header import decode_header
from datetime import datetime

from dateutil import parser


def format_email(raw_email: str) -> str:
    if '<' in raw_email:
        return re.split('<|>', raw_email)[1]
    return raw_email


def format_date(date: str) -> datetime:
    return parser.parse(date)


def format_subject(raw_subject: str) -> str:
    subject = decode_header(raw_subject)[0][0]
    if isinstance(subject, bytes):
        return decode_bytes(subject)
    return subject


def decode_bytes(subject: bytes) -> str:
    try:
        return subject.decode()
    except UnicodeDecodeError:
        return subject.decode('unicode_escape')


def format_uid(uid: bytes) -> bytes:
    return uid
