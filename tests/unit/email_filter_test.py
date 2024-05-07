from unittest.mock import Mock

import pytest

from nomail.email_filter import ListFilter


def email_mock_factory():
    mock = Mock()
    mock.sender = ''
    return mock


@pytest.mark.parametrize(
    ('sender', 'expected'),
    (
        (email_mock_factory(), False),
    ),
)
def test_filter_list(sender, expected):
    ListFilterMock = ListFilter()
    assert ListFilterMock.apply(sender) == expected
