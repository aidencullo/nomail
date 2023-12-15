class Email:
    """Hold email details and data"""

    def __init__(self, msg_data):
        self.recipient = msg_data['To']
        self.sender = msg_data['From']
        self.subject = msg_data['Subject']
        self.date = msg_data['Date']

    def __str__(self):
        return " \n".join([item for item in self.__dict__.values()])
