from abc import ABC, abstractmethod

from .adapter import EmailImapAdapter

class Action:
    """Action take on an email"""

    def __init__(self):
        self._imap = EmailImapAdapter()

    @abstractmethod
    def act(self, email):
        pass

class ActionDelete(Action):
    """Delete email"""

    def act(self, email):
        self._imap.delete_msg(email)
