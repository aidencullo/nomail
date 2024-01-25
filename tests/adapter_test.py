from unittest.mock import Mock, patch

from src.adapter import EmailImapAdapter


class TestAdapter:

    @patch("src.adapter.EmailImapAdapter.__init__", return_value=None)
    @patch("src.adapter.EmailImapAdapter.get_emails")
    def test_apply(self, get_emails_mock, imap_mock):

        # Arrange
        emails_mock = [0] * 10
        get_emails_mock.return_value = emails_mock
        test = Mock(return_value=True)
        email_filter_mock = Mock(test=test)
        adapter_mock = EmailImapAdapter()

        # Act
        result = adapter_mock.apply(email_filter_mock)

        # Assert
        assert result == emails_mock

    @patch("src.adapter.super")
    def test_delete_msg(self, super_mock):

        # Arrange
        adapter_mock = EmailImapAdapter()

        # Act
        adapter_mock.delete_msg(Mock())

        # Assert
        assert super_mock.called

    @patch("src.adapter.super")
    def test_copy_msg(self, super_mock):

        # Arrange
        adapter_mock = EmailImapAdapter()

        # Act
        adapter_mock.copy_msg(Mock())

        # Assert
        assert super_mock.called
