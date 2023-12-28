from unittest.mock import MagicMock, patch, create_autospec

import pytest

from src.action import (ActionDelete, ActionCopy, ActionPrint,
                        ActionMove, Action)
from src.email import Email

@patch("src.action.EmailImapAdapter.delete_msg")
def test_delete(delete_msg_mock):

    # Arrange
    action_delete = ActionDelete()
    mock_email = None

    # Act
    action_delete.act(mock_email)

    # Assert
    delete_msg_mock.assert_called_with(mock_email)


@patch("src.action.EmailImapAdapter.copy_msg")
def test_copy(copy_msg_mock):

    # Arrange
    action_copy = ActionCopy()
    mock_email = None

    # Act
    action_copy.act(mock_email)

    # Assert
    copy_msg_mock.assert_called_with(mock_email)


def test_print(capsys):

    # Arrange
    mock_email = create_autospec(Email)
    mock_email.sender = "test"
    action_print = ActionPrint()

    # Act
    action_print.act(mock_email)
    captured = capsys.readouterr()

    # Assert
    assert captured.out.strip() == str(mock_email.sender)

@patch("src.action.EmailImapAdapter.copy_msg")
@patch("src.action.EmailImapAdapter.delete_msg")
def test_move(delete_msg_mock, copy_msg_mock):

    # Arrange
    action_move = ActionMove()
    mock_email = None

    # Act
    action_move.act(mock_email)

    # Assert
    copy_msg_mock.assert_called_with(mock_email)
    delete_msg_mock.assert_called_with(mock_email)

def test_abstract():
    # Assert
    with pytest.raises(TypeError):
        # Act
        Action()
