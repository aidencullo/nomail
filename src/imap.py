from itertools import chain

import imaplib
import email

from .util import split_bytes, to_int
from .email import Email

RATE_LIMIT = 1
PROVIDER = "imap.gmail.com"

class Imap():
    """Access to imaplib library"""

    def __init__(self, credentials):
        self._imap = imaplib.IMAP4_SSL(PROVIDER)
        self._imap.login(*credentials)
        self._imap.select()

    # def __del__(self):
    #     self._imap.expunge()        
    
    def get_msg_data(self, uid):
        msg_bytes = self._imap.fetch(uid, "(RFC822)")[1][0][1]
        return email.message_from_bytes(msg_bytes)

    def get_uids(self, email_filter):
        _, [uids] = self._imap.search(None, "ALL")
        return split_bytes(uids)[:RATE_LIMIT]
    
    def get_msgs(self, email_filter):
        return [self.get_msg_data(uid) for uid in self.get_uids(email_filter)]

class EmailImapAdapter(Imap):
    
    def get_msgs(self, email_filter):
        return [Email(msg) for msg in super().get_msgs(email_filter)]

# class ImapWrapper(ABC):
#     """ Wrap imaplib internals """

#     @abstractmethod
#     def process(self):
#         pass
    
#     def __init__(self, username, password, senders):
#         self._imap = imaplib.IMAP4_SSL(PROVIDER)
#         self._imap.login(username, password)
#         self._imap.select()
#         self._msgs = self.get_msgs_for_emails(senders)

#     def __del__(self):
#         self._imap.expunge()        
    
#     def get_msgs_for_email(self, sender):
#         _, [uids] = self._imap.search(None, f'FROM {sender}')
#         return split_ids(uids)[:RATE_LIMIT]
    
#     def get_msgs_for_emails(self, senders):
#         return list(chain.from_iterable(self.get_msgs_for_email(sender) for sender in senders))

#     def get_content(self, uid):
#         msg_bytes = self._imap.fetch(uid, "(RFC822)")[1][0][1]
#         return format_data(email.message_from_bytes(msg_bytes))
    
#     def count(self):
#         print(f'count: {len(self._msgs)}')

# class ImapDeleter(ImapWrapper):
    
#     def process(self):
#         for uid in self._msgs:
#             # result = self._imap.store(uid, "+FLAGS", "\\Deleted")
#             yield self.get_content(uid)

# class ImapMover(ImapWrapper):
        
#     def process(self):
#         for uid in self._msgs:
#             # self._imap.copy(uid, "Trabajos")
#             # result = self._imap.store(uid, "+FLAGS", "\\Deleted")
#             yield self.get_content(uid)
