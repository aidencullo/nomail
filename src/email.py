from typing import List
from dataclasses import dataclass, field

import pandas as pd

from src import sanitize
from src import descriptor


class Email:

    uid = descriptor.Descriptor()

    def __init__(self, msg_data, uid):
        self.recipient = sanitize.format_email(msg_data['To'])
        self.sender = sanitize.format_email(msg_data['From'])
        self.subject = sanitize.format_subject(msg_data['Subject'])
        self.date = sanitize.format_date(msg_data['Date'])
        self.uid = sanitize.format_uid(uid)

    def __str__(self):
        return " \n".join([str(item) for item in self.__dict__.values()])

    def __iter__(self):
        yield self.subject



@dataclass(frozen=True)
class EmailList:
    emails: List[Email] = field(default_factory=list)

    def __iter__(self):
        for email in self.emails:
            yield email

    def to_df(self):
        return pd.DataFrame(self.emails)
