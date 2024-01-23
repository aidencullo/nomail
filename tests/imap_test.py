from unittest.mock import Mock, patch

import numpy as np
import pytest

from src.imap import Imap

MOCK_ARRAY_SIZE = 10
MOCK_ARRAY_ITEM = 0
MOCK_ARRAY = MOCK_ARRAY_SIZE * [MOCK_ARRAY_ITEM]
MOCK_BYTE_ARRAY = bytes(MOCK_ARRAY) 
MOCK_MSG = ""
MOCK_UID = 10


@pytest.fixture(name="mock_server_response")
def fixture_service_response():
    mock = np.zeros((2, 2, 2))
    mock.fill(MOCK_UID)
    return mock

@pytest.fixture(name="mock__imap")
def fixture__imap(mock_server_response):
    return Mock(return_value=mock_server_response)


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
    def test_fetch_msg_from_server(self, mock__imap):

        # Arrange
        imap_mock = Imap()
        imap_mock._imap.fetch = mock__imap

        # Act
        RESULT = imap_mock.fetch_msg_from_server(MOCK_UID)

        # Assert
        assert RESULT == MOCK_UID


    @patch("src.imap.imaplib", Mock())
    @patch("src.imap.split_bytes", return_value=MOCK_ARRAY, autospec=True)
    @patch("src.imap.Imap.fetch_uids_from_server", return_value=MOCK_BYTE_ARRAY ,autospec=True)
    def test_get_uids(self, mock_fetch_uids_from_server, mock_split_bytes):

        # Arrange
        imap_mock = Imap()

        # Act
        RESULT = imap_mock.get_uids()

        # Assert
        assert RESULT == MOCK_ARRAY
        mock_split_bytes.assert_called_once_with(MOCK_BYTE_ARRAY)
        mock_fetch_uids_from_server.assert_called_once()
