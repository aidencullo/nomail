from dataclasses import dataclass, field
from typing import Optional, Iterable

import pandas as pd

from .email_filter import Filter
from .email import Email


@dataclass
class EmailList:
    emails: list[Email] = field(default_factory=list)

    def __init__(self, emails: Optional[Iterable[Email]] = None):
        if emails is None:
            emails = []
        self.emails = list(emails)

    def __iter__(self):
        for email in self.emails:
            yield email

    def __getitem__(self, index):
        return self.emails[index]

    def __len__(self):
        return len(self.emails)

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.emails)
 
    def limit(self, rate_limit: int) -> 'EmailList':
        return EmailList(self[:rate_limit])
 
    def filter(self, email_filter: Filter) -> 'EmailList':
        return EmailList(email for email in self.emails if email_filter.apply(email))
