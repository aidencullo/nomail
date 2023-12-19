from .imap import Imap
from .email import Email

class EmailImapAdapter(Imap):
    """Adapter for imap class"""
    
    def __del__(self):
        print(f"deconstructing imap")
        super(DerivativeClass, self).__del__() 

    def get_msgs(self, email_filter):
        emails = [Email(msg, uid) for msg, uid in
        zip(super().get_msgs(),
        super().get_uids())]
        return [email for email in emails if email_filter.test(email)]
            
    def delete_msg(self, email):
        super().delete_msg(bytes(str(email.uid), 'ascii'))
            
    def move_msg(self, email):
        super().move_msg(bytes(str(email.uid), 'ascii'))

    def copy_msg(self, email):
        super().copy_msg(bytes(str(email.uid), 'ascii'))
        
