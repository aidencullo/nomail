from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from src import output

class TestOutput:

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), '2015/01/01/12:30:59.html'),
        (datetime(2015, 2, 1, 12, 30, 59, 0), '2015/02/01/12:30:59.html'),
        (datetime(2015, 1, 2, 12, 30, 30, 0), '2015/01/02/12:30:30.html'),
        (datetime(2019, 1, 2, 12, 30, 30, 0), '2019/01/02/12:30:30.html'),
    ),)
    @patch('src.output.datetime')
    def test_create_file_name(self, datetime_type_mock, datetime_mock,
                              expected):

        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        file_name = output.create_file_name()

        # Assert
        assert file_name == expected

    def test_print_file(self):
        pass
