from unittest.mock import patch
import imaplib

import pytest

from src import (action, email_filter, session, io, output)

@pytest.fixture(autouse=True)
def no_delay(imaplib_mock):
    with patch('src.imap.imaplib.IMAP4_SSL', return_value=imaplib_mock):
        yield


class TestEndToEnd:

    @pytest.mark.e2e
    def test_system(self, stub_email, email_binary, TEST_DATA_DIR):
        # Act
        gmail_session = session.Session()
        senders = io.read_csv(TEST_DATA_DIR / 'blacklist.csv')
        user_action = action.ActionNone()
        user_filter = email_filter.EmailFilterNone()
        [actual_email] = gmail_session.run(user_action, user_filter, rate_limit=1)

        # Assert
        assert actual_email == stub_email
