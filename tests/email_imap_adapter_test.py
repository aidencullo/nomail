from unittest.mock import Mock, patch, create_autospec

import pytest

from src.adapter import EmailImapAdapter
from src.email import Email
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

    @pytest.fixture(name="email_mock")
    def fixture_email(self):
        return create_autospec(Email)
    
    @patch("src.adapter.super", return_value=Mock())
    @patch("src.email.Email")
    def test_get_msgs(self, _, super_mock, email_imap_adapter_mock,
                      email_filter_mock):
        
        # Arrange
        super_class_mock = super_mock.return_value
        super_class_mock.get_msgs = Mock(return_value=[None])
        super_class_mock.get_uids = Mock(return_value=[None])

        # Act
        result = email_imap_adapter_mock.get_msgs(email_filter_mock)

        # Assert
        assert len(result) == 1

        
    @patch("src.adapter.super", return_value=Mock())
    def test_delete_msg(self, super_mock, email_mock, email_imap_adapter_mock):
        
        # Arrange
        super_class_mock = super_mock.return_value
        
        # Act
        email_imap_adapter_mock.delete_msg(email_mock)
        
        # Assert
        assert super_class_mock.delete_msg.called
        assert not super_class_mock.copy_msg.called
        assert not super_class_mock.get_msgs.called

    @patch("src.adapter.super", return_value=Mock())
    def test_copy_msg(self, super_mock, email_mock, email_imap_adapter_mock):
        
        # Arrange
        super_class_mock = super_mock.return_value
        
        # Act
        email_imap_adapter_mock.copy_msg(email_mock)
        
        # Assert
        assert super_class_mock.copy_msg.called
        assert not super_class_mock.delete_msg.called
        assert not super_class_mock.get_msgs.called
