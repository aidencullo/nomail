from nomail.util import split_bytes, to_int

import pytest


class TestUtil:
    @pytest.fixture
    def byte_str(self):
        return b'1 2 3 4 5'

    @pytest.fixture
    def byte_arr(self):
        return [b'1', b'2', b'3', b'4', b'5']

    @pytest.fixture
    def int_arr(self):
        return [1, 2, 3, 4, 5]

    def test_split_bytes(self, byte_str, byte_arr):
        result = split_bytes(byte_str)
        assert result == byte_arr

    def test_to_int(self, byte_arr, int_arr):
        result = to_int(byte_arr)
        assert result == int_arr
