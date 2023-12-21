from unittest.mock import MagicMock

import pytest

from src.action import (ActionDelete, ActionCopy, ActionPrint,
                        ActionMove, Action)
from src.adapter import EmailImapAdapter


# Arrange
@pytest.fixture(name="mocked_email")
def fixture_mocked_email():
    return MagicMock()


class TestActionDelete:
    def test_act(self, mocked_email):
        # Arrange
        action_delete = ActionDelete()
        email_adapter = EmailImapAdapter.instance()
        email_adapter.delete_msg = MagicMock()

        # Act
        action_delete.act(mocked_email)

        # Assert
        email_adapter.delete_msg.assert_called_once_with(mocked_email)


class TestActionCopy:
    def test_act(self, mocked_email):
        # Arrange
        action_copy = ActionCopy()
        email_adapter = EmailImapAdapter.instance()
        email_adapter.copy_msg = MagicMock()

        # Arrange
        action_copy.act(mocked_email)

        # Assert
        email_adapter.copy_msg.assert_called_once_with(mocked_email)


class TestActionPrint:
    def test_act(self, capsys, mocked_email):
        # Arrange
        action_print = ActionPrint()

        # Act
        action_print.act(mocked_email)
        captured = capsys.readouterr()

        # Assert
        assert captured.out.strip() == str(mocked_email.sender)


class TestActionMove:
    def test_act(self, mocked_email):
        # Arrange
        action_move = ActionMove()
        email_adapter = EmailImapAdapter.instance()
        email_adapter.copy_msg = MagicMock()
        email_adapter.delete_msg = MagicMock()

        # Act
        action_move.act(mocked_email)

        # Assert
        email_adapter.copy_msg.assert_called_once_with(mocked_email)
        email_adapter.delete_msg.assert_called_once_with(mocked_email)


class TestAction:
    def test_act(self, mocked_email):
        # Act & Assert
        with pytest.raises(TypeError):
            Action()
