import email
import imaplib
import pickle

from src.env import CREDENTIALS, PROVIDER, RATE_LIMIT
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
        return split_bytes(uids)[:RATE_LIMIT]

    def get_msgs(self):
        return [self.get_msg_data(uid) for uid in self.get_uids()]

    def delete_msg(self, uid):
        print(f"deleting {uid}")
        self._imap.store(uid, "+FLAGS", "\\Deleted")

    def copy_msg(self, uid):
        print(f"copying {uid}")
        self._imap.copy(uid, "Trabajos")
