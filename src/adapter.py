import src.email
from src.imap import Imap


class EmailImapAdapter(Imap):
    """Adapter for imap class"""

    def get_msgs(self, email_filter):
        emails = [src.email.Email(msg, uid) for msg, uid in
                  zip(super().get_msgs(),
                      super().get_uids())]
        return [email for email in emails if email_filter.test(email) == True]

    def delete_msg(self, email):
        super().delete_msg(bytes(str(email.uid), 'ascii'))

    def copy_msg(self, email):
        super().copy_msg(bytes(str(email.uid), 'ascii'))
