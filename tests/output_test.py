from datetime import datetime
from unittest.mock import Mock, patch

import pytest
import pandas as pd

from src import output


@pytest.fixture(name="df_mock")
def fixture_df():
    return pd.DataFrame({'col1': [1, 2], 'col2': [4, 3]})


class TestOutput:

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), 'logs/2015-01-01_12:30:59.csv'),
        (datetime(2015, 2, 1, 12, 30, 59, 0), 'logs/2015-02-01_12:30:59.csv'),
        (datetime(2015, 1, 2, 12, 30, 30, 0), 'logs/2015-01-02_12:30:30.csv'),
        (datetime(2019, 1, 2, 12, 30, 30, 0), 'logs/2019-01-02_12:30:30.csv'),
    ),)
    @patch('src.output.datetime')
    def test_generate_file_name(self, datetime_type_mock, datetime_mock,
                                expected):

        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        file_name = output.generate_file_name()

        # Assert
        assert file_name == expected

    @patch('src.output.generate_file_name')
    def test_write_df_to_file(self, mock_generate_file_name, df_mock):

        # Arrange
        mock_file_name = "sample.csv"
        mock_generate_file_name.return_value = mock_file_name

        # Act
        output.write_df_to_file(df_mock)

        # Assert
        assert df_mock.equals(pd.read_csv(mock_file_name))


    @patch('src.output.write_df_to_file')
    def test_write_emails_to_file(self, write_df_mock, df_mock):
        # Arrange
        email_list_mock = Mock()
        email_list_mock.to_df = Mock(return_value=df_mock)

        # Act
        output.write_emails_to_file(email_list_mock)

        # Assert
        write_df_mock.assert_called_with(df_mock)
