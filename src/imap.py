from itertools import chain

import imaplib
import email

from .util import split_bytes, to_int
from .env import RATE_LIMIT, PROVIDER, CREDENTIALS

class Imap():
    """Access to imaplib library"""

    def __init__(self, credentials=CREDENTIALS):
        self._imap = imaplib.IMAP4_SSL(PROVIDER)
        self._imap.login(*credentials)
        self._imap.select()

    def __del__(self):
        self._imap.expunge()        
    
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
        
    def move_msg(self, uid):
        print(f"moving {uid}")
        self._imap.copy(uid, "Trabajos")
        self._imap.store(uid, "+FLAGS", "\\Deleted")
