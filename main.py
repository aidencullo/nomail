from src.action import ActionDelete, ActionMove, ActionPrint
from src.filtering import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

# senders = read_csv('data/blacklist.csv')
senders = ['donotreply@email.schwab.com']

gmail_session.run(ActionMove(), EmailFilterList(senders))
