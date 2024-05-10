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

    def test_delete(self, imap_mock, email_dummy):
        delete_dummy = ActionDelete()
        delete_dummy.act(email_dummy)
        imap_mock.delete_msg.assert_called_with(email_dummy)

    def test_copy(self, imap_mock, email_dummy):
        copy_dummy = ActionCopy()
        copy_dummy.act(email_dummy)
        imap_mock.copy_msg.assert_called_with(email_dummy)

    def test_move(self, imap_mock, email_dummy):
        move_dummy = ActionMove()
        move_dummy.act(email_dummy)
        imap_mock.copy_msg.assert_called_with(email_dummy)
        imap_mock.delete_msg.assert_called_with(email_dummy)
