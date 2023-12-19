from src.action import ActionDelete, ActionPrint, ActionCopy, ActionMove
from src.filtering import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

senders = read_csv('data/blacklist.csv')

email_filter = EmailFilterNone()
actions = [ActionCopy(), ActionDelete()]
actions = [ActionMove()]

gmail_session.run(actions, email_filter)
