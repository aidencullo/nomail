from unittest.mock import Mock
import pickle

import pytest
from src.imap import Imap
from src.env import RATE_LIMIT


@pytest.fixture(name="imap_mock")
def fixture_imap():
    return Imap()


@pytest.fixture(name="byte_str_mock")
def fixture_byte_str():
    return b'1 2 3 4 5'


@pytest.fixture(name="imap_get_msgs_mock")
def fixture_imap_get_msgs(imap_mock):
    with open('data/email_bytes.pkl', 'rb') as f:
        msg_bytes_raw = pickle.load(f)
    msg_bytes = [None, [[None, msg_bytes_raw]]]
    imap_mock._imap.fetch = Mock(return_value=msg_bytes)
    return imap_mock


@pytest.fixture(name="imap_get_uids_mock")
def fixture_imap_get_uids(imap_mock, byte_str_mock):
    imap_mock._imap.search = Mock(return_value=(None, [byte_str_mock]))
    return imap_mock


class TestImap:

    def test_constructor(self, imap_mock):
        assert imap_mock._imap.close()

    def test_get_msg_data(self, imap_get_msgs_mock):

        # Arrange
        expected_str = "You can now move your Mint history to Credit Karma."

        # Act
        result = imap_get_msgs_mock.get_msg_data(1)

        # Assert
        assert result['Subject'] == expected_str
        imap_get_msgs_mock._imap.fetch.assert_called_with(1, '(RFC822)')

    def test_get_uids(self, imap_get_uids_mock):

        # Act
        result = imap_get_uids_mock.get_uids()

        # Assert
        assert len(result) == 5

    def test_get_msgs(self, imap_mock):

        # Arrange
        nones = [None] * 100
        imap_mock.get_msg_data = Mock(return_value=None)
        imap_mock.get_uids = Mock(return_value=nones)

        # Act
        result = imap_mock.get_msgs()

        # Assert
        assert result == nones

    def test_delete_msgs(self, imap_mock):

        # Arrange
        imap_mock._imap.store = Mock()
        uid = 1

        # Act
        imap_mock.delete_msg(uid)

        # Assert
        imap_mock._imap.store.assert_called_with(uid, "+FLAGS", "\\Deleted")

    def test_copy_msgs(self, imap_mock):

        # Arrange
        imap_mock._imap.copy = Mock()
        uid = 1

        # Act
        imap_mock.copy_msg(uid)

        # Assert
        imap_mock._imap.copy.assert_called_with(uid, "Trabajos")
