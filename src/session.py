from .adapter import EmailImapAdapter

class Session:
    """ Google email session """

    def __init__(self):
        self._imap = EmailImapAdapter()
 
    def run(self, action, email_filter):
        emails = self._imap.get_msgs(email_filter)
        for email in emails:
            action.act(email)
