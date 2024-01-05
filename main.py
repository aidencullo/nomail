from src.action import (ActionDelete, ActionPrint, ActionCopy,
                        ActionMove, ActionNone)
from src.email_filter import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

senders = read_csv('data/blacklist.csv')

email_filter = EmailFilterNone()
action = ActionNone()

gmail_session.run(action, email_filter)
