from email.message import Message

from . import imap
from .email import Email
from .emaillist import EmailList
from .email_filter import Filter


class EmailImapAdapter(imap.Imap):
    def __init__(self):
        super().__init__()

    def apply(self, email_filter: Filter, rate_limit: int = 1) -> EmailList:
        return self.get_emails().limit(rate_limit).filter(email_filter)

    def get_emails(self) -> EmailList:
        return EmailList([Email(msg, uid) for msg, uid in
                                zip(self.get_msgs(), self.get_uids())])

    def get_msgs(self) -> list[Message]:
        return super().get_msgs()

    def get_uids(self) -> list[bytes]:
        return super().get_uids()

    def delete_email(self, user_email: Email) -> None:
        super().delete_msg(bytes(str(user_email.uid), 'ascii'))

    def copy_email(self, user_email: Email) -> None:
        super().copy_msg(bytes(str(user_email.uid), 'ascii'))
