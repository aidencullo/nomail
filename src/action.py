"""
This module provides abstract base classes (ABC) and abstract
methods for defining interfaces to be implemented by concrete
classes. The ABC class and abstractmethod decorator are imported from
the 'abc' module.

Classes:
- ABC: Abstract Base Class, the base class for all other abstract base classes.
- abstractmethod: A decorator indicating that a method must be
  implemented by concrete subclasses.

Example usage:
    from abc import ABC, abstractmethod

    class MyAbstractClass(ABC):
        @abstractmethod
        def my_abstract_method(self):
            pass

    class MyConcreteClass(MyAbstractClass):
        def my_abstract_method(self):
            # Implementation of the abstract method
            pass

Note:
    It is recommended to inherit from ABC when creating abstract base
    classes and use the @abstractmethod decorator to define abstract
    methods that must be implemented by subclasses.

"""
from abc import ABC, abstractmethod

from .adapter import EmailImapAdapter


class Action(ABC):
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
