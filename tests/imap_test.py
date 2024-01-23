from unittest.mock import patch, Mock

import pytest
import numpy as np
from src.imap import Imap


MOCK_ARRAY_SIZE = 10
MOCK_ARRAY = 10 * [None]
MOCK_MSG = ""

class TestImap:


    @patch("src.imap.imaplib", autospec=True)
    @patch("src.imap.Imap.get_uids", return_value=(MOCK_ARRAY), autospec=True)
    @patch("src.imap.Imap.get_msg_data", return_value=None, autospec=True)
    def test_get_msgs(self, _1, _2, _3):

        # Arrange
        imap_mock = Imap()

        # Act
        RESULT = imap_mock.get_msgs()

        # Assert
        assert RESULT == [None] * MOCK_ARRAY_SIZE


    @patch("src.imap.imaplib", autospec=True)
    @patch("src.imap.email.message_from_bytes", return_value=MOCK_MSG, autospec=True)
    @patch("src.imap.Imap.fetch_msg_from_server", autospec=True)
    def test_get_msg_data(self, _1, _2, _3):

        # Arrange
        imap_mock = Imap()
        MOCK_UID = 10

        # Act
        RESULT = imap_mock.get_msg_data(MOCK_UID)

        # Assert
        assert RESULT == MOCK_MSG


    @patch("src.imap.imaplib", autospec=True)
    def test_fetch_msg_from_server(self, _):

        # Arrange
        MOCK_SERVER_MSG = 100
        MOCK_UID = 100
        mock_server_response = np.zeros((2, 2, 2))
        mock_server_response.fill(MOCK_SERVER_MSG)
        
        imap_mock = Imap()
        imap_mock._imap = Mock(fetch=Mock(return_value=mock_server_response))

        # Act
        RESULT = imap_mock.fetch_msg_from_server(MOCK_UID)

        # # Assert
        assert RESULT == MOCK_SERVER_MSG
