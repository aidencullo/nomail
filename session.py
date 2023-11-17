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
        email_details = []
        for sender in senders:
            try:
                status, messages = self._imap.search(None, f'FROM {sender}')
            except imaplib.IMAP4.error:
                print(f'no email from {sender} found')
                continue
            messages = messages[0].split(b' ')
            for mail in messages:
                status, msg = self._imap.fetch(mail, "(RFC822)")
                if status != 'OK':
                    raise ValueError('unexpected http response')
                for response in msg:
                    if isinstance(response, tuple):
                        msg = email.message_from_bytes(response[1])
                        message_details = {
                            'subject': sanitize.format_subject(msg["Subject"]),
                            'from': sanitize.format_email(msg["From"]),
                            'date': sanitize.format_date(msg["Date"]),
                        }
                    email_details.append(message_details)
                self._imap.store(mail, "+FLAGS", "\\Deleted")
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
