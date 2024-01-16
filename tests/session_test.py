from unittest.mock import Mock, patch

import pytest

from src.session import Session


@pytest.mark.skip(reason="dependent on env vars")
class TestSession:

    @patch('src.session.EmailImapAdapter.get_msgs')
    def test_run(self, mock_email_adapter_get_msgs):

        # Arrange
        session = Session()
        mock_email_adapter_get_msgs.return_value = [None]
        action_mock = Mock()

        # Act
        session.run(action_mock, None)

        # Assert
        assert action_mock.act.called
