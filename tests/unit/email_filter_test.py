from unittest.mock import Mock

import pytest

from nomail.email_filter import ListFilter


def email_mock_factory(sender):
    mock = Mock()
    mock.sender = sender
    return mock


@pytest.fixture(name="list_filter_mock")
def fixture_list_filter(sender_dummy):
    senders = ['person1', 'person2']
    return EmailFilterList(senders)


@pytest.mark.skip(reason="Skipping this CLASS level test")
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
    assert email_filter_mock.apply(sender) == expected
