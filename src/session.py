from src import adapter
from src import output
from src import email


class Session:

    def __init__(self):
        self._imap = adapter.EmailImapAdapter()

    def __del__(self):
        del self._imap

    def run(self, action, email_filter, rate_limit=10) -> email.EmailList:
        emails = self._imap.apply(email_filter, rate_limit=rate_limit)
        for email in reversed(emails):
            action.act(email)        
        print(f"{len(emails)} emails affected")
        return emails
