from .imap import EmailAdapter

class Session:
    """ Google email session """

    def __init__(self, credentials):
        self._imap = EmailAdapter(credentials)
 
    def run(self, action, email_filter):
        emails = self._imap.get_msgs(email_filter)
        for email in emails:
            action.act(email)
