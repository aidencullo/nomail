from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from src.output import create_file_name, format_data, print_file


@pytest.fixture(name='raw_unit_mock')
def fixture_raw_unit():
    return {
        'subject': None,
        'from': None,
        'date': None
    }


@pytest.fixture(name='raw_data_mock')
def fixture_raw_data(raw_unit_mock):
    return [raw_unit_mock]

class TestOutput:

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), '2015/01/01/12:30:59.html'),
    ),
                             )
    @patch('src.output.datetime')
    def test_create_file_name(self, datetime_type_mock, datetime_mock, expected):

        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        file_name = create_file_name()

        # Assert
        assert file_name == expected

    def test_format_data(self, raw_data_mock):

        # Act
        result = format_data(raw_data_mock)

        # Assert
        assert len(result) == len(raw_data_mock[0])
        assert len(result['subject']) == len(raw_data_mock)

    @patch('src.output.pd.DataFrame.to_html')
    def test_print_file(self, to_html_mock, raw_data_mock):

        # Act
        print_file(raw_data_mock)

        # Assert
        assert to_html_mock.called

    @patch('src.output.create_file_name')
    @patch('src.output.pd.DataFrame.to_html')
    def test_print_file_null_file_name(self, to_html_mock,
                                       create_file_name_mock, raw_data_mock):

        # Act
        print_file(raw_data_mock)

        # Assert
        assert create_file_name_mock.called

    @patch('src.output.create_file_name')
    @patch('src.output.pd.DataFrame.to_html')
    def test_print_file_present_file_name(self, to_html_mock,
                                          create_file_name_mock, raw_data_mock):

        # Act
        print_file(raw_data_mock, "")

        # Assert
        assert not create_file_name_mock.called
