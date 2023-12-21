from .adapter import EmailImapAdapter

class Session:
    """ Google email session """

    def __init__(self):
        self._imap = EmailImapAdapter.instance()

    def __del__(self):
        EmailImapAdapter.destroy()

    def run(self, action, email_filter):
        emails = self._imap.get_msgs(email_filter)
        for email in reversed(emails):
            action.act(email)
