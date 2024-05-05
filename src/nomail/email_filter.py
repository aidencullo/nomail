from typing import List, Optional

from .email import Email


class ListFilter():
    def __init__(self, address_list: Optional[List[str]] = None):
        if address_list is None:
            address_list = []
        self._address_list = address_list

    def apply(self, email: Email) -> bool:
        return email.sender in self._address_list
