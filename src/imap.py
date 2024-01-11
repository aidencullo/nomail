import email
import imaplib

from src.env import CREDENTIALS, PROVIDER
from src.util import split_bytes


class Imap():

    def __init__(self):
        self._imap = imaplib.IMAP4_SSL(PROVIDER)
        self._imap.login(*CREDENTIALS)
        self._imap.select()

    def get_msg_data(self, uid):
        msg_bytes = self._imap.fetch(uid, "(RFC822)")[1][0][1]
        return email.message_from_bytes(msg_bytes)

    def get_uids(self):
        _, [uids] = self._imap.search(None, "ALL")
        return split_bytes(uids)

    def get_msgs(self):
        return [self.get_msg_data(uid) for uid in self.get_uids()]

    def delete_msg(self, uid):
        print(f"moving {uid} to trash")
        self._imap.store(uid, '+X-GM-LABELS', '\\Trash')

    def copy_msg(self, uid):
        print(f"copying {uid} to Trabajos")
        self._imap.copy(uid, "Trabajos")
