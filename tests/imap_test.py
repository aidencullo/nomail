from unittest.mock import patch, Mock

import pytest
import numpy as np
from src.imap import Imap


MOCK_ARRAY_SIZE = 10
MOCK_UID = 10

# @pytest.fixture(name="byte_str_mock")
# def fixture_byte_str():
#     return b'1 2 3 4 5'

class TestImap:


    @patch("src.imap.Imap.__init__", return_value=None, autospec=True)
    @patch("src.imap.Imap.get_uids", return_value=([None] *
                                                   MOCK_ARRAY_SIZE), autospec=True)
    @patch("src.imap.Imap.get_msg_data", return_value=None, autospec=True)
    def test_get_msgs(self, mock_get_msg_data, mock_get_uids, imap_constructor_mock):

        # Arrange
        imap_mock = Imap()

        # Act
        result = imap_mock.get_msgs()

        # Assert
        assert result == [None] * MOCK_ARRAY_SIZE


    @patch("src.imap.Imap.__init__", return_value=None, autospec=True)
    @patch("src.imap.email.message_from_bytes", return_value="", autospec=True)
    @patch("src.imap.Imap.fetch_msg_from_server", autospec=True)
    def test_get_msg_data(self, mock_get_msg_data, mock_get_uids, imap_constructor_mock):

        # Arrange
        imap_mock = Imap()

        # Act
        result = imap_mock.get_msg_data(MOCK_UID)

        # Assert
        assert result == ""


    @patch("src.imap.Imap.__init__", return_value=None, autospec=True)
    def test_fetch_msg_from_server(self, imap_constructor_mock):
        pass
        # Arrange
        imap_mock = Imap()
        mock_server_msg = 100
        mock_uid = 100
        mock_server_response = np.zeros((2, 2, 2))
        mock_server_response.fill(mock_server_msg)
        imap_mock._imap = Mock(fetch=Mock(return_value=mock_server_response))

        # Act
        result = imap_mock.fetch_msg_from_server(mock_uid)

        # # Assert
        assert result == mock_server_msg
