from src.action import Action
from src.filtering import Filter
from src.session import Session
from src.environment import get_credentials
from src.io import read_csv

credentials = get_credentials()

gmail_session = Session(credentials)

senders = read_csv('data/blacklist.csv')

gmail_session.run(Action(), Filter())
