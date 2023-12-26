from unittest.mock import Mock, patch

import pytest

from src.adapter import EmailImapAdapter
import src.email
import src.imap
from src.filtering import EmailFilter


class TestEmailImapAdapter:

    # Arrange
    @pytest.fixture(name="email_imap_adapter_mock")
    def fixture_email_imap_adapter(self):
        return EmailImapAdapter.instance()

    @pytest.fixture(name="email_filter_mock")
    def fixture_email_filter(self):
        mock = Mock(return_value=True)
        return Mock(return_value=mock)

    @patch("src.adapter.super", return_value=Mock())
    @patch("src.email.Email")
    def test_get_msgs(self, _, super_mock, email_imap_adapter_mock,
                      email_filter_mock):
        
        # Arrange
        super_class_mock = super_mock.return_value
        # optimize this
        super_class_mock.get_msgs = Mock(return_value=[None])
        super_class_mock.get_uids = Mock(return_value=[None])

        # Act
        result = email_imap_adapter_mock.get_msgs(email_filter_mock)

        # Assert
        assert len(result) == 1

    # def test_delete_msg(self, email_imap_adapter):
    #     # Mock the underlying delete_msg method
    #     email_imap_adapter.delete_msg = lambda uid: None  # You might want to mock this to verify it's called correctly

    #     # Create a test email
    #     test_email = Email(b'Test Message', 123)

    #     # Call the method you want to test
    #     email_imap_adapter.delete_msg(test_email)

    #     # Add assertions based on your requirements

    # def test_copy_msg(self, email_imap_adapter):
    #     # Mock the underlying copy_msg method
    #     email_imap_adapter.copy_msg = lambda uid: None  # You might want to mock this to verify it's called correctly

    #     # Create a test email
    #     test_email = Email(b'Test Message', 123)

    #     # Call the method you want to test
    #     email_imap_adapter.copy_msg(test_email)

    #     # Add assertions based on your requirements
