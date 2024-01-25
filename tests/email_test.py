from datetime import datetime

import pendulum
import pytest
from unittest.mock import patch
# from unittest.mock import Mock

from src.email import Email

MOCK_UID = 1

# Arrange
@pytest.fixture(name="msg_data_mock")
def fixture_msg_data():
    return {
        'To': 'culloaiden3@gmail.com',
        'From': 'Mint <mint@em2.mint.intuit.com>',
        'Subject': 'You can now move your Mint history to Credit Karma.',
        'Date': 'Wed, 20 Dec 2023 23:53:03 +0000 (UTC)',
    }


# @pytest.fixture(name="msg_data_sanitized_mock")
# def fixture_msg_data_sanitized():
#     return {
#         'To': 'culloaiden3@gmail.com',
#         'From': 'mint@em2.mint.intuit.com',
#         'Subject': 'You can now move your Mint history to Credit Karma.',
#         'Date': datetime(2023, 12, 20, 23, 53, 3),
#     }


@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'


# @pytest.fixture(name="msg_uid_sanitized_mock")
# def fixture_msg_uid_sanitized():
#     return 1


@patch("src.email.sanitize")
def test_constructor(mock_sanitize, msg_data_mock, msg_uid_mock):

    # Arrange
    mock_sanitize.format_email.return_value = ""
    mock_sanitize.format_subject.return_value = ""
    mock_sanitize.format_date.return_value = datetime.now()
    mock_sanitize.format_uid.return_value = MOCK_UID


    # Act
    email = Email(msg_data_mock, msg_uid_mock)

    # Assert
    assert hasattr(email, 'recipient')
    assert hasattr(email, 'sender')
    assert hasattr(email, 'subject')
    assert hasattr(email, 'date')
    assert hasattr(email, 'uid')

    mock_sanitize.format_email.assert_called()
    mock_sanitize.format_subject.assert_called_once()
    mock_sanitize.format_date.assert_called_once()
    mock_sanitize.format_uid.assert_called_once()
