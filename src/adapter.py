from src.email import Email
from src.imap import Imap


class EmailImapAdapter(Imap):

    def __init__(self):
        super().__init__()
    
    def apply(self, email_filter):
        return [email for email in self.get_emails() if email_filter.test(email)]

    def get_emails(self):
        return [Email(msg, uid) for msg, uid in zip(self.get_msgs(), self.get_uids())]
    
    def get_msgs(self):
        return super().get_msgs()

    def get_uids(self):
        return super().get_uids()

    def delete_msg(self, email):
        super().delete_msg(bytes(str(email.uid), 'ascii'))

    def copy_msg(self, email):
        super().copy_msg(bytes(str(email.uid), 'ascii'))    
