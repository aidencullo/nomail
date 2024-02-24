from typing import Optional

from src import (adapter, output, email, action, email_filter)


class Session:

    def __init__(self) -> None:
        self._imap: adapter.EmailImapAdapter = adapter.EmailImapAdapter()

    def __del__(self):
        del self._imap

    def run(self, user_action: action.Action,
            user_email_filter: email_filter.EmailFilter,
            rate_limit: Optional[int] = 10) -> email.EmailList:
        emails = self._imap.apply(user_email_filter, rate_limit=rate_limit)
        self.act(emails, user_action)
        return emails

    def act(self, emails, user_action):
        for email in emails[::-1]:
            user_action.act(email)
