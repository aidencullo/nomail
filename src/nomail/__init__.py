# read version from installed package
from importlib.metadata import version
__version__ = version("nomail")

__all__ = [
    'filter',
]

def filter():
    print(f'{__name__=}')
