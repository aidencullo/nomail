from src.action import (ActionDelete, ActionPrint, ActionCopy,
ActionMove, Action)
from src.filtering import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

senders = read_csv('data/blacklist.csv')

email_filter = EmailFilterNone()
# action = ActionMove()
# action = ActionDelete()
action = ActionPrint()
action = Action()

# gmail_session.run(action, email_filter)
