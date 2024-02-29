from unittest.mock import patch
import imaplib

import pytest

from src.action import ActionNone
from src.email_filter import EmailFilterNone
from src.session import run
from src.io import read_csv

@pytest.fixture(autouse=True)
def no_delay(imaplib_mock):
    with patch('src.imap.imaplib.IMAP4_SSL', return_value=imaplib_mock):
        yield


@pytest.mark.e2e
class TestEndToEnd:

    def test_null_filter_single_item(self, stub_email, email_binary, TEST_DATA_DIR):
        # Act
        senders = read_csv(TEST_DATA_DIR / 'blacklist.csv')
        [actual_email] = run(ActionNone(), EmailFilterNone(), rate_limit=1)
        # Assert
        assert actual_email == stub_email
