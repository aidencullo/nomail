import email
import imaplib

from .env import CREDENTIALS, PROVIDER
from .util import split_bytes


class Imap():

    def __init__(self):
        try:
            self._imap = imaplib.IMAP4_SSL(PROVIDER)
        except ConnectionRefusedError as e:
            raise e
            print("couldn't connect to imap email server")
            print("this is most likely due to incorrect credentials, check your env file")
            return
        self._imap.login(*CREDENTIALS)
        self._imap.select()

    def get_msgs(self):
        return [self.get_msg_data(uid) for uid in self.get_uids()]        
        
    def get_msg_data(self, uid):
        return email.message_from_bytes(self.fetch_msg_from_server(uid))

    def fetch_msg_from_server(self, uid):
        return self._imap.fetch(uid, "(RFC822)")[1][0][1]

    def get_uids(self):
        return split_bytes(self.fetch_uids_from_server())

    def fetch_uids_from_server(self):
        return self._imap.search(None, "ALL")[1][0]
 
    def fetch_noop_from_server(self) -> None:
        print(self._imap.noop())
   
    def delete_msg(self, uid):
        self._imap.store(uid, '+X-GM-LABELS', '\\Trash')

    def copy_msg(self, uid):
        self._imap.copy(uid, "Trabajos")
