# read version from installed package
from importlib.metadata import version
from . import session
from .action import ActionNone
from .email_filter import EmailFilterNone

__version__ = version("nomail")

__all__ = [
    'filter',
    'noop',
]

def filter():
    try:
        with open('blacklist.csv') as f:
            blacklist = f.read().splitlines()
    except FileNotFoundError:
        print("blacklist.csv not found")
        blacklist = []
    emails_processed = session.run(ActionNone(), EmailFilterNone())
    print(f'{emails_processed} emails processed')

def noop():
    session.connect()
