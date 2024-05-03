import email
import imaplib
from typing import List, Optional

from .env import CREDENTIALS, PROVIDER
from .util import split_bytes


class Imap():

    def __init__(self):
        try:
            self._imap = imaplib.IMAP4_SSL(PROVIDER)
        except ConnectionRefusedError as e:
            print("couldn't connect to imap email server")
            print("this is most likely due to incorrect credentials, check your env file")
            return
        except BaseException as e:
            print(f'{e=}')
            print(f'PROVIDER={PROVIDER}')
            raise e
        self._imap.login(*CREDENTIALS)
        self._imap.select()

    def get_msgs(self) -> List[str]:
        return [self.get_msg_data(uid) for uid in self.get_uids()]

    def get_msg_data(self, uid: int) -> str:
        return email.message_from_bytes(self.fetch_msg_from_server(uid))

    def fetch_msg_from_server(self, uid: int) -> bytes:
        return self._imap.fetch(uid, "(RFC822)")[1][0][1]

    def get_uids(self) -> List[int]:
        return split_bytes(self.fetch_uids_from_server())

    def fetch_uids_from_server(self) -> bytes:
        sender = "no-reply@computrabajo.com"
        email = f'FROM {sender}'
        ids = self._imap.search(None, email)[1][0]
        return ids
        # return self._imap.search(None, "ALL")[1][0]

    def noop(self) -> None:
        print(self._imap.noop())

    def delete_msg(self, uid: int) -> None:
        self._imap.store(uid, '+X-GM-LABELS', '\\Trash')

    def copy_msg(self, uid: int) -> None:
        self._imap.copy(uid, "Trabajos")
