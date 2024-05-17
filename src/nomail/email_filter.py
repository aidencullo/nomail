from typing import Optional

from .email import Email


class Filter():
    def apply(self, email: Email) -> bool:
        return True


class ListFilter(Filter):
    def __init__(self, address_list: Optional[list[str]] = None):
        if address_list is None:
            address_list = []
        self._address_list = address_list

    def apply(self, email: Email) -> bool:
        print(f'{email.sender=} {self._address_list=}')
        return email.sender in self._address_list


class NullFilter(Filter):
    def apply(self, email: Email) -> bool:
        return email.sender
