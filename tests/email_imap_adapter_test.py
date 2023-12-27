from unittest.mock import Mock, patch, create_autospec
from unittest import TestCase

import pytest

from src.adapter import EmailImapAdapter
from src.email import Email
import src.imap
from src.filtering import EmailFilter


@patch("src.adapter.super")
@patch("src.email.Email")
class TestEmailImapAdapter:

    # Arrange
    # SUT
    @pytest.fixture(name="email_imap_adapter")
    def fixture_email_imap_adapter(self):
        return EmailImapAdapter()

    @pytest.fixture(name="email_filter_mock")
    def fixture_email_filter(self):
        return Mock(test=Mock(return_value=True))

    def test_get_msgs(self, _, super_mock, email_imap_adapter,
                      email_filter_mock):

        # Arrange
        super_class_mock = Mock()
        super_class_mock.get_msgs = Mock(return_value=[None])
        super_class_mock.get_uids = Mock(return_value=[None])
        super_mock.return_value = super_class_mock

        # Act
        result = email_imap_adapter.get_msgs(email_filter_mock)

        # Assert
        assert len(result) == 1

    def test_delete_msg(self, email_mock, super_mock, email_imap_adapter):
        
        # Arrange
        super_class_mock = super_mock.return_value
        
        # Act
        email_imap_adapter.delete_msg(email_mock)
        
        # Assert
        assert super_class_mock.delete_msg.called
        assert not super_class_mock.copy_msg.called
        assert not super_class_mock.get_msgs.called

    def test_copy_msg(self, email_mock, super_mock, email_imap_adapter):
        
        # Arrange
        super_class_mock = super_mock.return_value
        
        # Act
        email_imap_adapter.copy_msg(email_mock)
        
        # Assert
        assert super_class_mock.copy_msg.called
        assert not super_class_mock.delete_msg.called
        assert not super_class_mock.get_msgs.called
