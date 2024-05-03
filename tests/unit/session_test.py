from unittest.mock import patch

import pytest

from nomail.session import run


@pytest.fixture(name="mock_emails")
def fixture_emails():
    return [None] * 10

@pytest.mark.skip(reason="Skipping this CLASS level test")
class TestSession:
    @patch('nomail.action.Action', autospec=True)
    @patch('nomail.email_filter.EmailFilter', autospec=True)
    @patch('nomail.session.EmailImapAdapter', autospec=True)
    def test_run(self, mock_email_imap_adapter, mock_email_filter, mock_action, mock_emails):
        mock_apply = mock_email_imap_adapter.return_value.apply
        mock_apply.return_value = mock_emails
        run(mock_action, mock_email_filter)
        mock_apply.assert_called()
        mock_action.act.assert_called()
