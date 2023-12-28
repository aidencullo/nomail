from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from src.email import Email


# Arrange
@pytest.fixture(name="msg_data_mock")
def fixture_msg_data():
    return {
        'To': 'culloaiden3@gmail.com',
        'From': 'Mint <mint@em2.mint.intuit.com>',
        'Subject': 'You can now move your Mint history to Credit Karma.',
        'Date': 'Wed, 20 Dec 2023 23:53:03 +0000 (UTC)',
    }

@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'


def test_attributes(msg_data_mock, msg_uid_mock):

    # Act
    email = Email(msg_data_mock, msg_uid_mock)

    # Assert
    assert hasattr(email, 'date')
    assert hasattr(email, 'sender')
    assert hasattr(email, 'recipient')
    assert hasattr(email, 'subject')
    assert hasattr(email, 'uid')

@patch('src.email.sanitize')
def test_sanitize_calls(sanitize_mock, msg_data_mock, msg_uid_mock):

    # Arrange
    sanitize_mock.format_email = Mock(return_value="")
    sanitize_mock.format_subject = Mock(return_value="")
    sanitize_mock.format_date = Mock(return_value=datetime.today())
    sanitize_mock.format_uid = Mock(return_value=1)

    # Act
    Email(msg_data_mock, msg_uid_mock)

    # Assert
    assert sanitize_mock.format_email.called
    assert sanitize_mock.format_subject.called
    assert sanitize_mock.format_date.called
    assert sanitize_mock.format_uid.called
