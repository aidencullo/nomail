from datetime import datetime
from unittest.mock import patch

import pytest
import pandas as pd

from src.email import Email, EmailList


MOCK_UID = 1

@pytest.fixture(name="subject_mock")
def fixture_subject():
    return 'You can now move your Mint history to Credit Karma.'

@pytest.fixture(name="msg_data_mock")
def fixture_msg_data(subject_mock):
    return {
        'To': 'culloaiden3@gmail.com',
        'From': 'Mint <mint@em2.mint.intuit.com>',
        'Subject': subject_mock,
        'Date': 'Wed, 20 Dec 2023 23:53:03 +0000 (UTC)',
    }


@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'
 
@pytest.fixture(name="email_mock")
def fixture_email(msg_data_mock, msg_uid_mock):
    return Email(msg_data_mock, msg_uid_mock)

@pytest.fixture(name="email_list_mock")
def fixture_email_list(email_mock):
    return EmailList([email_mock] * 2)


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


def test_emails_to_df(email_list_mock, subject_mock):

    # Act
    df = email_list_mock.to_df()

    # Assert
    assert df.iloc[1, 0] == subject_mock
