from unittest.mock import patch

import pytest

from nomail.action import ActionCopy, ActionDelete, ActionMove
from nomail.email import Email


class TestAction:
    @pytest.fixture
    def email_dummy(self):
        data = {
            'To': 'culloaiden3@gmail.com',
            'From': '"Reed.co.uk" <no-reply@jobs.reed.co.uk>',
            'Subject': "Added today: new Permanent 'Software Developer' Jobs | Rochester Jobs & Vacancies...",
            'Date': 'Wed, 31 Jan 2024 03:04:13 +0000',
        }
        return Email(data, b'1')

    @pytest.fixture
    def imap_mock(self):
        patcher = patch('nomail.action.Imap')
        return patcher.start().return_value

    @pytest.fixture
    def delete_msg_mock(self, imap_mock):
        return imap_mock.delete_msg

    @pytest.fixture
    def copy_msg_mock(self, imap_mock):
        return imap_mock.copy_msg

    @pytest.fixture
    def move_msg_mock(self, imap_mock):
        return imap_mock.move_msg

    def test_delete(self, email_dummy, delete_msg_mock):
        delete_dummy = ActionDelete()
        delete_dummy.act(email_dummy)
        delete_msg_mock.assert_called

    def test_copy(self, email_dummy, copy_msg_mock):
        copy_dummy = ActionCopy()
        copy_dummy.act(email_dummy)
        copy_msg_mock.assert_called

    def test_move(self, email_dummy, move_msg_mock):
        move_dummy = ActionMove()
        move_dummy.act(email_dummy)
        move_msg_mock.assert_called
