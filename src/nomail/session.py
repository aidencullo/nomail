from .action import Action
from .adapter import EmailImapAdapter
from .emaillist import EmailList
from .email_filter import ListFilter


def run(action: Action, filter: ListFilter, rate_limit: int = 1) -> EmailList:
    _imap: EmailImapAdapter = EmailImapAdapter()
    emails = _imap.apply(filter, rate_limit)
    act(emails, action)
    return emails


def act(emails: EmailList, action: Action) -> None:
    for email in emails[::-1]:
        action.act(email)


def noop() -> None:
    _imap: EmailImapAdapter = EmailImapAdapter()
    _imap.noop()
