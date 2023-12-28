from unittest.mock import Mock, patch

import pytest

from src.adapter import EmailImapAdapter


@patch("src.adapter.Imap.copy_msg")
@patch("src.adapter.Imap.delete_msg")
@patch("src.adapter.Imap.get_uids")
@patch("src.adapter.Imap.get_msgs")
@patch("src.email.Email")
class TestAdapter:

    # Arrange
    # SUT
    @pytest.fixture(name="email_imap_adapter")
    def fixture_email_imap_adapter(self):
        return EmailImapAdapter()

    @pytest.fixture(name="email_filter_mock")
    def fixture_email_filter(self):
        return Mock(test=Mock(return_value=True))

    def test_get_msgs(self, email_mock, get_msgs_mock, get_uids_mock,
                      delete_msg_mock, copy_msg_mock,
                      email_imap_adapter, email_filter_mock):

        # Arrange
        get_uids_mock.return_value = [None]
        get_msgs_mock.return_value = [None]

        # Act
        result = email_imap_adapter.get_msgs(email_filter_mock)

        # Assert
        assert len(result) == 1
        assert get_uids_mock.called
        assert get_msgs_mock.called
        assert not delete_msg_mock.called
        assert not copy_msg_mock.called

    def test_delete_msg(self, email_mock, get_msgs_mock, get_uids_mock,
                        delete_msg_mock, copy_msg_mock,
                        email_imap_adapter, email_filter_mock):

        # Act
        email_imap_adapter.delete_msg(email_mock)

        # Assert
        assert not get_uids_mock.called
        assert not get_msgs_mock.called
        assert delete_msg_mock.called
        assert not copy_msg_mock.called

    def test_copy_msg(self, email_mock, get_msgs_mock, get_uids_mock,
                      delete_msg_mock, copy_msg_mock,
                      email_imap_adapter, email_filter_mock):

        # Act
        email_imap_adapter.copy_msg(email_mock)

        # Assert
        assert not get_uids_mock.called
        assert not get_msgs_mock.called
        assert not delete_msg_mock.called
        assert copy_msg_mock.called
