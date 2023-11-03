import imaplib
import email
from email.header import decode_header
import os
import sys
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def filter_out_encodings(str):
    return [x for x in str if x[1] != 'utf-8']

def decode(str):
    if isinstance(str, bytes):
        return str.decode()
    return str

def first_five(str):
    return ' '.join(str.split()[:5])

def filter_header(message_array):
    filtered_message_array = filter_out_encodings(message_array)
    message = filtered_message_array[0][0]
    message = decode(message)
    message = message.strip()
    message = first_five(message)
    return message

# account credentials
username = "culloaiden3@gmail.com"
password = "fexd pmwg epkf yrfy"

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
            subject = filter_header(decode_header(msg["Subject"]))
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

# my functions
