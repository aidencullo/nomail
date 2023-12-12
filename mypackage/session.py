from itertools import chain

import email

from .imap_ops import ImapWrapper


class Session:
    """ Google email session """

    def __init__(self, username, password):
        self._imap = ImapWrapper(username, password)
 
    def delete(self, senders):
        return list(chain.from_iterable(self.delete_sender(sender) for
                                        sender in senders))

    def delete_sender(self, sender):
        return [self.delete_msg(msg_id) for msg_id in self._imap.get_ids(sender)]
    
    def delete_msg(self, msg_id):
        return self._imap.delete_msg(msg_id)

    def move(self, senders):
        return list(chain.from_iterable(self.move_sender(sender) for
                                        sender in senders))

    def move_sender(self, sender):
        return [self.move_msg(msg_id) for msg_id in self._imap.get_ids(sender)]
    
    def move_msg(self, msg_id):
        return self._imap.move_msg(msg_id)
