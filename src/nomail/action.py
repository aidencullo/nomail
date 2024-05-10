from abc import ABC, abstractmethod

from .imap import Imap
from .email import Email


class Action(ABC):
    def __init__(self):
        self._imap = Imap()

    @abstractmethod
    def act(self, email: Email) -> None:
        pass


class ActionDelete(Action):
    def act(self, email: Email) -> None:
        self._imap.delete_msg(email)


class ActionCopy(Action):
    def act(self, email: Email) -> None:
        self._imap.copy_msg(email)


class ActionMove(Action):
    def act(self, email: Email) -> None:
        self._imap.copy_msg(email)
        self._imap.delete_msg(email)


class ActionNone(Action):
    def act(self, email: Email) -> None:
        pass
