from unittest.mock import create_autospec, patch

import pytest

from src.action import (Action, ActionCopy, ActionDelete, ActionMove,
                        ActionPrint)
from src.email import Email


@patch("src.action.EmailImapAdapter")
def test_delete(adapter_mock):

    # Arrange
    action_delete = ActionDelete()

    # Act
    action_delete.act(None)

    # Assert
    adapter_mock.return_value.delete_msg.assert_called_with(None)


@patch("src.action.EmailImapAdapter")
def test_copy(adapter_mock):

    # Arrange
    action_copy = ActionCopy()

    # Act
    action_copy.act(None)

    # Assert
    adapter_mock.return_value.copy_msg.assert_called_with(None)


@patch("src.action.EmailImapAdapter")
def test_print(adapter_mock, capsys):

    # Arrange
    mock_email = create_autospec(Email)
    mock_email.sender = "test"
    action_print = ActionPrint()

    # Act
    action_print.act(mock_email)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.strip() == str(mock_email.sender)


@patch("src.action.EmailImapAdapter")
def test_move(adapter_mock):

    # Arrange
    action_move = ActionMove()

    # Act
    action_move.act(None)

    # Assert
    adapter_mock.return_value.copy_msg.assert_called_with(None)
    adapter_mock.return_value.delete_msg.assert_called_with(None)


def test_abstract():
    # Assert
    with pytest.raises(TypeError):
        # Act
        Action()
