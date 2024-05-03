from datetime import datetime
from unittest.mock import Mock, patch

import pytest
import pandas as pd

from nomail import output


@pytest.fixture(name="df_mock")
def fixture_df():
    return pd.DataFrame({'col1': [1, 2], 'col2': [4, 3]})


@pytest.mark.skip(reason="Skipping this CLASS level test")
class TestOutput:

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), 'logs/2015-01-01_12:30:59'),
        (datetime(2015, 2, 1, 12, 30, 59, 0), 'logs/2015-02-01_12:30:59'),
        (datetime(2015, 1, 2, 12, 30, 30, 0), 'logs/2015-01-02_12:30:30'),
        (datetime(2019, 1, 2, 12, 30, 30, 0), 'logs/2019-01-02_12:30:30'),
    ),)
    @patch('nomail.output.datetime')
    def test_generate_file_name(self, datetime_type_mock, datetime_mock,
                                expected):
        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        file_name = output.generate_file_name()

        # Assert
        assert file_name == expected

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), 'logs/2015-01-01_12:30:59.csv'),
        (datetime(2015, 2, 1, 12, 30, 59, 0), 'logs/2015-02-01_12:30:59.csv'),
        (datetime(2015, 1, 2, 12, 30, 30, 0), 'logs/2015-01-02_12:30:30.csv'),
        (datetime(2019, 1, 2, 12, 30, 30, 0), 'logs/2019-01-02_12:30:30.csv'),
    ),)
    @patch('nomail.output.datetime')
    def test_generate_csv_name(self, datetime_type_mock, datetime_mock,
                                expected):
        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        csv_name = output.generate_csv_name()

        # Assert
        assert csv_name == expected

    @pytest.mark.parametrize('datetime_mock, expected', (
        (datetime(2015, 1, 1, 12, 30, 59, 0), 'logs/2015-01-01_12:30:59.html'),
        (datetime(2015, 2, 1, 12, 30, 59, 0), 'logs/2015-02-01_12:30:59.html'),
        (datetime(2015, 1, 2, 12, 30, 30, 0), 'logs/2015-01-02_12:30:30.html'),
        (datetime(2019, 1, 2, 12, 30, 30, 0), 'logs/2019-01-02_12:30:30.html'),
    ),)
    @patch('nomail.output.datetime')
    def test_generate_html_name(self, datetime_type_mock, datetime_mock,
                                expected):
        # Arrange
        datetime_type_mock.today = Mock(return_value=datetime_mock)

        # Act
        html_name = output.generate_html_name()

        # Assert
        assert html_name == expected
        
    @patch('nomail.output.generate_file_name')
    def test_write_df_to_csv(self, mock_generate_file_name, df_mock):
        # Arrange
        mock_file_name = "sample.csv"
        mock_generate_file_name.return_value = mock_file_name

        # Act
        output.write_df_to_csv(df_mock)

        # Assert
        assert df_mock.equals(pd.read_csv(mock_file_name))


    @patch('nomail.output.write_df_to_csv')
    def test_write_emails_to_csv(self, write_df_mock, df_mock):
        # Arrange
        email_list_mock = Mock()
        email_list_mock.to_df = Mock(return_value=df_mock)

        # Act
        output.write_emails_to_csv(email_list_mock)

        # Assert
        write_df_mock.assert_called_with(df_mock)


    @patch('nomail.output.generate_file_name')
    def test_write_df_to_html(self, mock_generate_file_name, df_mock):
        # Arrange
        mock_file_name = "sample.html"
        mock_generate_file_name.return_value = mock_file_name

        # Act
        output.write_df_to_html(df_mock)

        # Assert
        
        [html_df] = pd.read_html(mock_file_name)
        assert df_mock.equals(html_df)


    @patch('nomail.output.write_df_to_html')
    def test_write_emails_to_html(self, write_df_mock, df_mock):
        # Arrange
        email_list_mock = Mock()
        email_list_mock.to_df = Mock(return_value=df_mock)

        # Act
        output.write_emails_to_html(email_list_mock)

        # Assert
        write_df_mock.assert_called_with(df_mock)
