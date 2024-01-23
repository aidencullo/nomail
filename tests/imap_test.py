from unittest.mock import patch, Mock

import numpy as np
from src.imap import Imap


MOCK_ARRAY_SIZE = 10
MOCK_ARRAY_ITEM = None
MOCK_ARRAY = MOCK_ARRAY_SIZE * [MOCK_ARRAY_ITEM]
MOCK_MSG = ""
MOCK_UID = 10

class TestImap:


    @patch("src.imap.imaplib", Mock())
    @patch("src.imap.Imap.get_uids", autospec=True)
    @patch("src.imap.Imap.get_msg_data", autospec=True)
    def test_get_msgs(self, mock_get_msg_data, mock_get_uids):

        # Arrange
        imap_mock = Imap()
        mock_get_uids.return_value = MOCK_ARRAY
        mock_get_msg_data.return_value = MOCK_ARRAY_ITEM
        
        # Act
        RESULT = imap_mock.get_msgs()

        # Assert
        assert RESULT == MOCK_ARRAY


    @patch("src.imap.imaplib", Mock())
    @patch("src.imap.email.message_from_bytes", autospec=True)
    @patch("src.imap.Imap.fetch_msg_from_server", autospec=True)
    def test_get_msg_data(self, mock_fetch_msg_from_server, mock_message_from_bytes):

        # Arrange
        imap_mock = Imap()
        mock_message_from_bytes.return_value=MOCK_MSG

        # Act
        RESULT = imap_mock.get_msg_data(MOCK_UID)

        # Assert
        assert RESULT == MOCK_MSG


    @patch("src.imap.imaplib", Mock())
    def test_fetch_msg_from_server(self):

        # Arrange
        mock_server_response = np.zeros((2, 2, 2))
        mock_server_response.fill(MOCK_UID)
        
        imap_mock = Imap()
        imap_mock._imap = Mock(fetch=Mock(return_value=mock_server_response))

        # Act
        RESULT = imap_mock.fetch_msg_from_server(MOCK_UID)

        # # Assert
        assert RESULT == MOCK_UID
