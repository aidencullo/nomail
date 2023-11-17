import re

def extract_email(raw):
    items = raw.split()
    for item in items:
        if '@' in item:
            email = item
    email = re.sub('[<>]',"", email)
    return email
