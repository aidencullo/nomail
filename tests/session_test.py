from unittest.mock import patch

import pytest

from src.session import Session


@pytest.fixture(name="mock_emails")
def fixture_emails():
    return [None] * 10

class TestSession:

    @patch('src.action.Action', autospec=True)
    @patch('src.email_filter.EmailFilter', autospec=True)
    @patch('src.session.EmailImapAdapter', autospec=True)
    def test_run(self, mock_email_imap_adapter, mock_email_filter, mock_action, mock_emails):

        # Arrange
        session = Session()
        mock_apply = mock_email_imap_adapter.return_value.apply
        mock_apply.return_value = mock_emails

        # Act
        session.run(mock_action, mock_email_filter)

        # Assert
        mock_apply.assert_called_once_with(mock_email_filter)
        mock_action.act.assert_called()
