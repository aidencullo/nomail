from src.adapter import EmailImapAdapter


class Session:

    def __init__(self):
        self._imap = EmailImapAdapter()

    def __del__(self):
        del self._imap

    def run(self, action, email_filter, rate_limit=10):
        emails = self._imap.apply(email_filter, rate_limit=rate_limit)
        for email in reversed(emails):
            action.act(email)
        print(f"{len(emails)} emails affected")
