from unittest.mock import Mock, patch

import pytest

from nomail.adapter import EmailImapAdapter


class TestAdapter:
    @pytest.mark.skip(reason="Skipping this CLASS level test")
    @patch("nomail.adapter.EmailImapAdapter.__init__", return_value=None)
    @patch("nomail.adapter.EmailImapAdapter.get_emails")
    def test_apply(self, get_emails_mock, imap_mock, email_list_mock):

        # Arrange        
        get_emails_mock.return_value = email_list_mock
        test = Mock(return_value=True)
        email_filter_mock = Mock(test=test)
        adapter_mock = EmailImapAdapter()

        filtered_emails = adapter_mock.apply(email_filter_mock)

        assert filtered_emails == expected_emails

    @pytest.mark.skip(reason="Skipping this CLASS level test")
    @patch("nomail.adapter.super")
    def test_delete_msg(self, super_mock):

        # Arrange
        adapter_mock = EmailImapAdapter()

        # Act
        adapter_mock.delete_msg(Mock())

        # Assert
        assert super_mock.called

    @pytest.mark.skip(reason="Skipping this CLASS level test")
    @patch("nomail.adapter.super")
    def test_copy_msg(self, super_mock):

        # Arrange
        adapter_mock = EmailImapAdapter()

        # Act
        adapter_mock.copy_msg(Mock())

        # Assert
        assert super_mock.called
