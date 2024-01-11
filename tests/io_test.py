from unittest.mock import Mock, patch

import numpy as np

from src.io import read_csv, write_csv


class TestIO:

    @patch('src.io.pd.DataFrame')
    def test_write_csv(self, data_frame_mock):

        # Arrange
        data_frame_mock.return_value = Mock()
        file_name_mock = "test file"
        data_mock = "data"

        # Act
        write_csv(data_mock, file_name_mock)

        # Assert
        data_frame_mock.assert_called_with(data_mock)
        data_frame_mock.return_value.to_csv.assert_called_with(file_name_mock)

    @patch('src.io.pd.read_csv')
    def test_read_csv(self, pd_read_csv_mock):

        # Arrange
        df_mock = np.array([Mock()] * 10).reshape(10, 1)
        pd_read_csv_mock.return_value = Mock(iloc=df_mock)
        file_name_mock = "test file"

        # Act
        result = read_csv(file_name_mock)

        # Assert
        pd_read_csv_mock.assert_called_with(file_name_mock)
        assert len(result) == len(df_mock)
