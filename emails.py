import imaplib
import email
from email.header import decode_header
import os
import sys
from dotenv import load_dotenv

import filtering

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.select("INBOX")

sender = "info@email.meetup.com"
# search for specific mails by sender
status, messages = imap.search(None, f'FROM {sender}')

# to get all mails
# status, messages = imap.search(None, "ALL")

# convert messages to a list of email IDs
messages = messages[0].split(b' ')

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    # you can delete the for loop for performance if you have a long list of emails
    # because it is only for printing the SUBJECT of target email to delete
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = filtering.filter_header(decode_header(msg["Subject"]))
            if isinstance(subject, bytes):
                # if it's a bytes type, decode to str
                subject = subject.decode()
            print(f'deleting {subject}')
    # mark the mail as deleted
    # imap.store(mail, "+FLAGS", "\\Deleted")
 
# don't think this is necessary

# # permanently remove mails that are marked as deleted
# # from the selected mailbox (in this case, INBOX)
# # imap.expunge()
# # close the mailbox
# imap.close()
# # logout from the account
# imap.logout()
