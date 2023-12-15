from itertools import chain

import imaplib
import email

from .util import split_ids
from .sanitize import format_data

RATE_LIMIT = 5
PROVIDER = "imap.gmail.com"

class Imap():
    """Access to imaplib library"""

    def __init__(self, credentials):
        pass

    # def __del__(self):
    #     self._imap.expunge()        
    
    def get_msgs(self, email_filter):
        return []

class EmailAdapter(Imap):
    pass

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
#         _, [msg_ids] = self._imap.search(None, f'FROM {sender}')
#         return split_ids(msg_ids)[:RATE_LIMIT]
    
#     def get_msgs_for_emails(self, senders):
#         return list(chain.from_iterable(self.get_msgs_for_email(sender) for sender in senders))

#     def get_content(self, msg_id):
#         msg_bytes = self._imap.fetch(msg_id, "(RFC822)")[1][0][1]
#         return format_data(email.message_from_bytes(msg_bytes))
    
#     def count(self):
#         print(f'count: {len(self._msgs)}')

# class ImapDeleter(ImapWrapper):
    
#     def process(self):
#         for msg_id in self._msgs:
#             # result = self._imap.store(msg_id, "+FLAGS", "\\Deleted")
#             yield self.get_content(msg_id)

# class ImapMover(ImapWrapper):
        
#     def process(self):
#         for msg_id in self._msgs:
#             # self._imap.copy(msg_id, "Trabajos")
#             # result = self._imap.store(msg_id, "+FLAGS", "\\Deleted")
#             yield self.get_content(msg_id)
