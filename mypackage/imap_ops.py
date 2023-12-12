import imaplib

from .util import split_ids

RATE_LIMIT = 5


class ImapWrapper:
    """ Hide imaplib internals """
    
    def __init__(self, username, password, provider="imap.gmail.com"):
        self._imap = imaplib.IMAP4_SSL(provider)
        self._imap.login(username, password)
        self._imap.select()

    def __del__(self):
        self._imap.expunge()        

    def get_ids(self, sender):
        _, [msg_ids] = self._imap.search(None, f'FROM {sender}')
        return split_ids(msg_ids)[:RATE_LIMIT]
    
    def delete_msg(self, msg_id):        
        self._imap.store(msg_id, "+FLAGS", "\\Deleted")
        
    def move_msg(self, msg_id):
        self._imap.copy(msg_id, "Trabajos")
        self.delete_msg(msg_id)
