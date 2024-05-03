from nomail.util import split_bytes, to_int


class TestUtil:

    def test_split_bytes(self):

        # Arrange
        byte_str = b'1 2 3 4 5'
        expected = [b'1', b'2', b'3', b'4', b'5']

        # Act
        result = split_bytes(byte_str)
        # Assert
        assert result == expected

    def test_to_int(self):

        # Arrange
        byte = [b'1']
        expected = [1]

        # Act
        result = to_int(byte)
        # Assert
        assert result == expected
