from src import sanitize
from src.descriptor import Descriptor


class Email:

    uid = Descriptor()

    def __init__(self, msg_data, uid):
        self.recipient = sanitize.format_email(msg_data['To'])
        self.sender = sanitize.format_email(msg_data['From'])
        self.subject = sanitize.format_subject(msg_data['Subject'])
        self.date = sanitize.format_date(msg_data['Date'])
        self.uid = sanitize.format_uid(uid)

    def __str__(self):
        return " \n".join([str(item) for item in self.__dict__.values()])
