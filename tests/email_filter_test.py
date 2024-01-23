from unittest.mock import Mock

import pytest

from src.email_filter import EmailFilterAll, EmailFilterList, EmailFilterNone


def email_mock_factory(sender):
    mock = Mock()
    mock.sender = sender
    return mock


@pytest.fixture(name="email_filter_mock")
def fixture_email_filter():
    senders = ['person1', 'person2']
    return EmailFilterList(senders)


@pytest.mark.parametrize(
    ('email_filter', 'expected'),
    (
        (EmailFilterNone(), True),
        (EmailFilterAll(), False),
    ),
)
def test_email_filter_binary(email_filter, expected):

    # Assert
    assert email_filter.test(None) == expected


@pytest.mark.parametrize(
    ('sender', 'expected'),
    (
        (email_mock_factory('person1'), True),
        (email_mock_factory('person2'), True),
        (email_mock_factory('person3'), False),
        (email_mock_factory(''), False),
    ),
)
def test_email_filter_list(sender, expected, email_filter_mock):

    # Assert
    assert email_filter_mock.test(sender) == expected
