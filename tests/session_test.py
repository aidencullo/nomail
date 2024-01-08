import pytest
from unittest.mock import Mock, patch

from src.session import Session


@pytest.fixture(name='session')
def fixture_session():
    return Session()


class TestSession:

    def test_run(self, session):
        # def run(self, action, email_filter):
        # Act
        action_mock = Mock
        session.run(action_mock, Mock())

        assert action_mock.called
