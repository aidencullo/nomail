import email
import imaplib
from email.message import Message

from .env import CREDENTIALS, PROVIDER
from .util import split_bytes


class Imap:
    def __init__(self):
        try:
            self._imap = imaplib.IMAP4_SSL(PROVIDER)
        except ConnectionRefusedError as e:
            print("couldn't connect to imap email server")
            print("this is most likely due to incorrect credentials, check your env file")
            raise e
        except BaseException as e:
            print(f'{e=}')
            print(f'PROVIDER={PROVIDER}')
            raise e
        self._imap.login(*CREDENTIALS)
        self._imap.select()

    def get_msgs(self) -> list[Message]:
        return [self.get_msg_data(uid) for uid in self.get_uids()]

    def get_msg_data(self, uid: bytes) -> Message:
        fetched = self.fetch_msg_from_server(uid)
        email_message = email.message_from_bytes(fetched)
        print(f'{email_message["From"]=}')
        return email_message

    def fetch_msg_from_server(self, uid: bytes) -> bytes:
        typ, data = self._imap.fetch(uid, '(RFC822)')
        return data[0][1]

    def get_uids(self) -> list[bytes]:
        return self.fetch_uids_from_server()

    def fetch_uids_from_server(self) -> bytes:
        M = self._imap
        typ, data = M.search(None, 'ALL')
        throttle = 5
        data = data[0].split()[::-1][:throttle]
        return data

    def noop(self) -> None:
        print(self._imap.noop())

    def delete_msg(self, uid: bytes) -> None:
        self._imap.store(uid, '+X-GM-LABELS', '\\Trash')

    def copy_msg(self, uid: bytes) -> None:
        self._imap.copy(uid, "Trabajos")
