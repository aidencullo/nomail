from src.action import ActionDelete, ActionMove, ActionPrint, ActionCopy
from src.filtering import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

senders = read_csv('data/blacklist.csv')

email_filter = EmailFilterNone()
action_copy = ActionCopy()
action_delete = ActionDelete()

gmail_session.run(action_copy, email_filter)
gmail_session.run(action_delete, email_filter)
