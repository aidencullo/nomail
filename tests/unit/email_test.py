from datetime import datetime
from unittest.mock import patch


from nomail.email import Email


@patch("nomail.email.sanitize")
def test_constructor(mock_sanitize, msg_data_mock, msg_uid_mock):

    # Arrange
    mock_sanitize.format_email.return_value = ""
    mock_sanitize.format_subject.return_value = ""
    mock_sanitize.format_date.return_value = datetime.now()
    mock_sanitize.format_uid.return_value = 1


    # Act
    email = Email(msg_data_mock, msg_uid_mock)

    # Assert
    assert hasattr(email, 'recipient')
    assert hasattr(email, 'sender')
    assert hasattr(email, 'subject')
    assert hasattr(email, 'date')
    assert hasattr(email, 'uid')


def test_emails_to_df(email_list_mock, subject_mock, sender_mock):

    # Act
    df = email_list_mock.to_df()

    # Assert
    assert df.iloc[1, 0] == (subject_mock, sender_mock)
