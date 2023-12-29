from datetime import datetime

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


@pytest.fixture(name="msg_data_sanitized_mock")
def fixture_msg_data_sanitized():
    return {
        'To': 'culloaiden3@gmail.com',
        'From': 'mint@em2.mint.intuit.com',
        'Subject': 'You can now move your Mint history to Credit Karma.',
        'Date': datetime(2023, 12, 20, 18, 53, 3),
    }


@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'


@pytest.fixture(name="msg_uid_sanitized_mock")
def fixture_msg_uid_sanitized():
    return 1


def test_attributes(msg_data_mock, msg_data_sanitized_mock,
                    msg_uid_mock, msg_uid_sanitized_mock):

    # Act
    email = Email(msg_data_mock, msg_uid_mock)

    # Assert
    assert email.recipient == msg_data_sanitized_mock['To']
    assert email.sender == msg_data_sanitized_mock['From']
    assert email.subject == msg_data_sanitized_mock['Subject']
    assert email.date == msg_data_sanitized_mock['Date']
    assert email.uid == msg_uid_sanitized_mock
