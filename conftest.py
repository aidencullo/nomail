from pathlib import Path

import pytest
from unittest.mock import patch, Mock

from src.email import Email, EmailList

@pytest.fixture(name='TEST_DATA_DIR')
def fixture_data_path():
    return Path(__file__).resolve().parent / 'data'


@pytest.fixture(name="msg_uid_mock")
def fixture_msg_uid():
    return b'1'


@pytest.fixture(name="subject_mock")
def fixture_subject():
    return 'You can now move your Mint history to Credit Karma.'


@pytest.fixture(name="sender_mock")
def fixture_sender():
    return 'mint@em2.mint.intuit.com'


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


@pytest.fixture(name="stub_email")
def fixture_stub_email():
    data = {
        'To': 'culloaiden3@gmail.com',
        'From': '"Reed.co.uk" <no-reply@jobs.reed.co.uk>',
        'Subject': "Added today: new Permanent 'Software Developer' Jobs | Rochester Jobs & Vacancies...",
        'Date': 'Wed, 31 Jan 2024 03:04:13 +0000',
    }
    return Email(data, b'1')


@pytest.fixture(name="email_binary")
def fixture_binary(TEST_DATA_DIR):
    file_name = TEST_DATA_DIR / 'email.bin'
    with open(file_name, 'rb') as f:
        contents = f.read()
    return contents


@pytest.fixture(name="imaplib_mock")
def fixture_imaplib(email_binary):
    imaplib_mock = Mock()
    imaplib_mock.search = Mock(return_value=[None, [b'1']])
    imaplib_mock.fetch = Mock(return_value=[None, [[None, email_binary]]])
    return imaplib_mock
