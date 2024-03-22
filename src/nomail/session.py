from typing import Optional

from .adapter import EmailImapAdapter
from .email_filter import EmailFilter
from .email import EmailList
from .action import Action

def run(action: Action, filter: EmailFilter, rate_limit: int=1) -> EmailList:
    _imap: EmailImapAdapter = EmailImapAdapter()
    emails = _imap.apply(filter, rate_limit)
    act(emails, action)
    return emails

def act(emails, action):
    for email in emails[::-1]:
        action.act(email)

def connect():
    _imap: EmailImapAdapter = EmailImapAdapter()
    _imap.fetch_noop_from_server()
