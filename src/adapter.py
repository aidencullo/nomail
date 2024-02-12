from src import (email, imap)


class EmailImapAdapter(imap.Imap):

    def __init__(self):
        super().__init__()

    def apply(self, email_filter, rate_limit=1000):
        return [email for email in self.get_emails()[:rate_limit] if
                email_filter.test(email)]

    def get_emails(self) -> email.EmailList:
        return email.EmailList([email.Email(msg, uid) for msg, uid in
                                zip(self.get_msgs(), self.get_uids())])

    def get_msgs(self):
        return super().get_msgs()

    def get_uids(self):
        return super().get_uids()

    def delete_msg(self, email):
        super().delete_msg(bytes(str(email.uid), 'ascii'))

    def copy_msg(self, email):
        super().copy_msg(bytes(str(email.uid), 'ascii'))
