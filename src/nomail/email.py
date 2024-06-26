from . import sanitize


class Email:

    recipient: str
    sender: str
    subject: str
    date: str
    uid: int

    def __init__(self, msg_data: list[str], uid: bytes):
        self.recipient = sanitize.format_email(msg_data['To'])
        self.sender = sanitize.format_email(msg_data['From'])
        self.subject = sanitize.format_subject(msg_data['Subject'])
        self.date = sanitize.format_date(msg_data['Date'])
        self.uid = sanitize.format_uid(uid)

    def __repr__(self):
        return " \n".join([str(item) for item in self.__dict__.values()])

    def __iter__(self):
        yield self.subject, self.sender

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__
