from .sanitize import format_date, format_email, format_subject, format_uid
from .descriptors import Descriptor

class Email:
    """Hold email details and data"""

    uid = Descriptor()

    def __init__(self, msg_data, uid):
        self.recipient = format_email(msg_data['To'])
        self.sender = format_email(msg_data['From'])
        self.subject = msg_data['Subject']
        self.date = format_date(msg_data['Date'])
        self.uid = format_uid(uid)

    def __str__(self):
        return " \n".join([str(item) for item in self.__dict__.values()])
