from unittest.mock import Mock, patch

import pytest

from src.email import Email

class TestEmail:

    @pytest.fixture(name="mock_msg_data")
    def fixture_email_filter(self):
        return 0
    
    def test_email(self):
        assert 1
        # email = Email(mock_msg_data, mock_uid)
