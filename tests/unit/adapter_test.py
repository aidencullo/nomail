from unittest.mock import Mock, patch

import pytest

from nomail.adapter import EmailImapAdapter
from nomail.email_filter import NullFilter
from nomail.emaillist import EmailList


@pytest.fixture(name="adapter")
def adapter():
    return EmailImapAdapter()

@pytest.fixture(name="empty_list")
def empty_list():
    return EmailList([])

@pytest.fixture
def get_emails():
    patcher = patch('nomail.adapter.EmailImapAdapter.get_emails')
    return patcher.start()

class TestAdapter:
    @patch('nomail.adapter.imap.imaplib')
    def test_apply(self, imaplib, get_emails, empty_list):
        adapter = EmailImapAdapter()
        get_emails.return_value = empty_list
        expected_emails = empty_list

        filtered_emails = adapter.apply(NullFilter())

        assert filtered_emails == expected_emails
