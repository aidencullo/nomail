from importlib.metadata import version

from .action import ActionNone
from .email_filter import ListFilter
from .session import run

__version__ = version("nomail")


def filter(rate_limit: int = 1):
    blacklist = get_blacklist()
    emails = run(ActionNone(), ListFilter(blacklist), rate_limit)
    print_summary(emails)


def get_blacklist() -> list[str]:
    with open('blacklist.csv') as file:
        return file.read().splitlines()
        

def print_summary(emails):
    print(f"{len(emails)} email{plural(emails)} processed")


def print_summary_verbose(emails):
    print(f'{emails=} ')
    print_summary(emails)


def plural(emails):
    return 's' if len(emails) != 1 else ''
