import imaplib
import email
from email.header import decode_header

import filtering

class Filter:
    def __init__(self, username, password):
        self._imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self._imap.login(username, password)
        self._imap.select("INBOX")

    def delete_emails(self, sender):
        status, messages = self._imap.search(None, f'FROM {sender}')
        data = []
        messages = messages[0].split(b' ')
        for mail in messages:
            status, msg = self._imap.fetch(mail, "(RFC822)")
            if status != 'OK':
                raise ValueError('unexpected http response')
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    email_details = {
                        'subject': msg["Subject"],
                        'from': msg["From"],
                        'to': msg["To"],
                        'date': msg["Date"],
                    }
                    # subject = filtering.filter_header(decode_header(msg["Subject"]))
                    # if isinstance(subject, bytes):
                    #     subject = subject.decode()
                    data.append(email_details)
        return data
