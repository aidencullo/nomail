from importlib.metadata import version
from .session import noop
from .action import ActionNone
from .email_filter import ListFilter


__version__ = version("nomail")


def filter(rate_limit: int = 1):
    blacklist = get_blacklist()
    emails = session.run(ActionNone(), ListFilter(blacklist), rate_limit)
    print_summary(emails)


def get_blacklist():
    try:
        with open('blacklist.csv') as f:
            blacklist = f.read().splitlines()
    except FileNotFoundError:
        print("blacklist.csv not found")
        blacklist = []
    return blacklist
        

def print_summary(emails):
    print(f"{len(emails)} email{plural(emails)} processed")


def print_summary_verbose(emails):
    print(f'{emails=} ')
    print_summary(emails)


def plural(emails):
    return 's' if len(emails) != 1 else ''
