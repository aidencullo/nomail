from abc import ABC, abstractmethod

from .adapter import EmailImapAdapter

class Action:
    """Action take on an email"""

    def __init__(self):
        self._imap = EmailImapAdapter.instance()

    @abstractmethod
    def act(self, email):
        pass

class ActionDelete(Action):
    """Delete email"""

    def act(self, email):
        self._imap.delete_msg(email)

class ActionCopy(Action):
    """Copy email"""

    def act(self, email):
        self._imap.copy_msg(email)

class ActionPrint(Action):
    """Print email"""

    def act(self, email):
        print(email.sender)

class ActionMove(Action):
    """Move email"""

    def act(self, email):
        self._imap.copy_msg(email)
        self._imap.delete_msg(email)
