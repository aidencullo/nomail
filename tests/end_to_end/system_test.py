from unittest.mock import patch, Mock
import imaplib

import pytest

from src import (action, email_filter, session, io, output, email)

@pytest.fixture(autouse=True)
def no_delay(fixture_imaplib):
    with patch('src.imap.imaplib.IMAP4_SSL', return_value=fixture_imaplib):
        yield


class TestEndToEnd:

    @pytest.mark.e2e
    def test_system(self, email1_mock, email_binary, TEST_DATA_DIR):
        # Act
        gmail_session = session.Session()
        senders = io.read_csv(TEST_DATA_DIR / 'blacklist.csv')
        user_action = action.ActionNone()
        user_filter = email_filter.EmailFilterNone()
        [email] = gmail_session.run(user_action, user_filter, rate_limit=1)

        # Assert
        assert email == email1_mock
