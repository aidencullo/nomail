from src.action import ActionDelete
from src.filtering import EmailFilterAll, EmailFilterNone, EmailFilterList
from src.session import Session
from src.io import read_csv

gmail_session = Session()

senders = read_csv('data/blacklist.csv')
senders = ['PayPal@emails.paypal.com']

gmail_session.run(ActionDelete(), EmailFilterList(senders))
