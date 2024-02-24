from pathlib import Path
from unittest.mock import patch, Mock
import imaplib

import pytest

from src import (action, email_filter, session, io, output, email)

TEST_DATA_DIR = Path(__file__).resolve().parent.parent.parent / 'data'

class TestEndToEnd:

    @pytest.mark.e2e
    @patch('src.imap.imaplib.IMAP4_SSL')
    def test_system(self, mock_imaplib):
        # Arrange
        test_mock = Mock()
        test_mock.search = Mock(return_value=[None, [b'1']])

        file_name = TEST_DATA_DIR / 'afile.txt'

        with open(file_name, 'rb') as f:
            contents = f.read()
            
        test_mock.fetch = Mock(return_value=[None, [[None, contents]]])
        mock_imaplib.return_value = test_mock

        # Act
        gmail_session = session.Session()
        senders = io.read_csv(TEST_DATA_DIR / 'blacklist.csv')
        user_action = action.ActionNone()
        user_filter = email_filter.EmailFilterNone()
        [email] = gmail_session.run(user_action, user_filter, rate_limit=1)

        # Assert
        assert email.recipient == 'culloaiden3@gmail.com'
        assert email.subject == 'Re: Saying hello'
