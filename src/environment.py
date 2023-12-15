import os
from collections import namedtuple

from dotenv import load_dotenv

Credentials = namedtuple('Credentials', ['username', 'password'])

def get_credentials():
    load_dotenv()
    return Credentials(os.getenv('USERNAME'), os.getenv('PASSWORD'))
