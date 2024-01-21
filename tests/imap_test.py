from unittest.mock import patch

import pytest
from src.imap import Imap


MOCK_ARRAY_SIZE = 10

@pytest.fixture(name="byte_str_mock")
def fixture_byte_str():
    return b'1 2 3 4 5'

class TestImap:


    @patch("src.imap.Imap.__init__", return_value=None)
    @patch("src.imap.Imap.get_uids", return_value=([None] * MOCK_ARRAY_SIZE))
    @patch("src.imap.Imap.get_msg_data", return_value=None)
    def test_get_msgs(self, mock_get_msg_data, mock_get_uids, imap_constructor_mock):

        # Arrange
        imap_mock = Imap()

        # Act
        result = imap_mock.get_msgs()

        # Assert
        assert result == [None] * MOCK_ARRAY_SIZE
