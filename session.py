import imaplib
import email
from email.header import decode_header

import filtering
import sanitize

class Session:
    def __init__(self, username, password):
        self._imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self._imap.login(username, password)
        self._imap.select("INBOX")

    def delete_emails(self, senders):
        senders = senders[:100]
        email_details = []
        for sender in senders:
            status, messages = self._imap.search(None, f'FROM {sender}')
            messages = messages[0].split(b' ')
            messages = [message for message in messages if message != b'']
            for mail in messages:
                status, msg = self._imap.fetch(mail, "(RFC822)")
                if status != 'OK':
                    raise ValueError('unexpected http response')
                msg = [response for response in msg if isinstance(response, tuple)]
                [response] = msg
                msg = email.message_from_bytes(response[1])
                message_details = sanitize.format_data(msg)
                email_details.append(message_details)                    
                # self._imap.store(mail, "+FLAGS", "\\Deleted")
        return email_details

    def collect_emails(self):
        senders = set()
        status, messages = self._imap.search(None, "ALL")
        messages = messages[0].split(b' ')
        for mail in messages:
            status, msg = self._imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    sender = msg["From"]
                    sender = sanitize.extract_email(sender)
                    senders.add(sender)
        return senders

    def count_emails(self):
        status, messages = self._imap.search(None, "ALL")
        messages = messages[0].split(b' ')
        return len(messages)
