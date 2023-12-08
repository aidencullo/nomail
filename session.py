import imaplib
import email
import email.message

import filtering
import sanitize

class Session:
    """ Google email session """
    def __init__(self, username, password, provider="imap.gmail.com", folder="INBOX"):
        self._imap = imaplib.IMAP4_SSL(provider)
        self._imap.login(username, password)
        self._imap.select(folder)

    def split_if_full(self, byte_str):
        return byte_str.split(b' ') if byte_str else []

    def get_msg_ids_from_sender(self, sender: str) -> list:
        _, [msg_ids] = self._imap.search(None, f'FROM {sender}')
        return self.get_msg_ids(f'FROM {sender}')

    def get_msg_ids_from_all(self) -> list:
        return self.get_msg_ids()

    def get_msg_ids(self, desc="ALL") -> list:
        _, [msg_ids] = self._imap.search(None, desc)
        return self.split_if_full(msg_ids)

    def get_msg_from_id(self, msg_id: int) -> email.message.Message:
        msg_bytes = self._imap.fetch(msg_id, "(RFC822)")[1][0][1]
        return email.message_from_bytes(msg_bytes)

    def delete_emails(self, senders):
        emails = []
        for sender in senders:
            msg_ids = self.get_msg_ids_from_sender(sender)
            for msg_id in msg_ids:
                emails.append(sanitize.format_data(self.get_msg_from_id(msg_id)))
                self._imap.store(msg_id, "+FLAGS", "\\Deleted")
        self._imap.expunge()
        print(f'deleting {len(emails)} emails')
        return emails

    def collect_emails(self):
        msg_ids = self.get_msg_ids_from_all()
        for msg_id in msg_ids:
            yield sanitize.format_email(self.get_msg_from_id(msg_id))
        # return senders

    def count_emails(self, sender=None, folder="inbox"):
        msg_ids = self.get_msg_ids_from_all()
        print(f'there are {len(msg_ids)} emails in {folder}')
