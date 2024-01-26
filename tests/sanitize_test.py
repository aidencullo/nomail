import datetime

from src.sanitize import format_date, format_email, format_subject, format_uid


class TestSanitize:

    def test_format_email(self):

        # Arrange
        raw_email = '<test@test.com>'
        sanitized_email = 'test@test.com'

        # Act
        result = format_email(raw_email)

        assert result == sanitized_email

    def test_format_date(self):

        # Arrange
        raw_date = 'Wed, 20 Dec 2023 23:53:03 +0000 (UTC)'
        sanitized_date = datetime.datetime(2023, 12, 20, 23, 53, 3, tzinfo=datetime.timezone.utc)

        # Act
        result = format_date(raw_date)

        assert result == sanitized_date

    def test_format_subject(self):

        # Arrange
        raw_subject = 'You can now move your Mint history to Credit Karma.'
        sanitized_subject = 'You can now move your Mint history to Credit Karma.'

        # Act
        result = format_subject(raw_subject)

        assert result == sanitized_subject

    def test_format_uid(self):

        # Arrange
        raw_uid = 1

        # Act
        result = format_uid(raw_uid)

        assert result == raw_uid
