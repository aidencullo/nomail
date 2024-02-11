import pytest
from src.email import Email, EmailList


@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'


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


@pytest.fixture(name="email_mock")
def fixture_email(msg_data_mock, msg_uid_mock):
    return Email(msg_data_mock, msg_uid_mock)


@pytest.fixture(name="email_list_mock")
def fixture_email_list(email_mock):
    return EmailList([email_mock] * 2)
