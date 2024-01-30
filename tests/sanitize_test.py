import datetime

import pytest

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

    @pytest.mark.parametrize(
        ('subject', 'expected'),
        [
            ('You can now move your Mint history to Credit Karma.', 'You can now move your Mint history to Credit Karma.'),
            ('=?ISO-8859-1?Q?Ya_puedes_actualizar_el_n=FAme?=\r\n\
        =?ISO-8859-1?Q?ro_de_tel=E9fono_de_tu_Apple=A0ID?=', 'Ya puedes actualizar el número de teléfono de tu Apple ID'),
            ('You\'re invited to create a Patient Portal account at Optum, formerly Caremount Medical.',
             'You\'re invited to create a Patient Portal account at Optum, formerly Caremount Medical.'),
            ('Time for your appointment!','Time for your appointment!'),
            ('Added today: new Permanent \'Software Developer\' Jobs | Rochester Jobs & Vacancies...','Added today: new Permanent \'Software Developer\' Jobs | Rochester Jobs & Vacancies...'),
            ('How was your experience at Optum?','How was your experience at Optum?'),
            ('[GitHub] Your Dependabot alerts for the week of Jan 23 - Jan 30','[GitHub] Your Dependabot alerts for the week of Jan 23 - Jan 30'),
            ('=?utf-8?B?SGVsbG8sIGdvbGRlbiBnb29kbmVzcyDinKg=?= ','Hello, golden goodness ✨  '),
            ('=?utf-8?B?SW50ZWxsaVNlYXJjaOKEoiBBbGVydCBmb3VuZCAxMzUgbmV3IGpv?==?utf-8?B?YnMsIGJhc2VkIG9uIHlvdXIgcHJvZmlsZSA=?=','IntelliSearch™ Alert found 135 new jobs, based on your profile '),
            ('Your Health Summary','Your Health Summary'),
            ('Results from your recent Optum Visit','Results from your recent Optum Visit'),
            ('Instantly get 3 free months by referring a friend','Instantly get 3 free months by referring a friend'),
            ('=?utf-8?Q?=C3=9ALTIMA=20PREVENTA=20PARA=20CAMDEN?=','ÚLTIMA PREVENTA PARA CAMDEN'),
            ('=?UTF-8?q?4-Unit_Vacation_Rental_in_New_York_=F0=9F=8C=87_26%_Initial_Ren?==?UTF-8?q?tal_Yield_|_Managed_by_Airbnb_Superhost?=','4-Unit Vacation Rental in New York 🌇 26% Initial Rental Yield | Managed by Airbnb Superhost'),
            ('=?ISO-8859-1?Q?Ya_puedes_actualizar_el_n=FAme?==?ISO-8859-1?Q?ro_de_tel=E9fono_de_tu_Apple=A0ID?=','Ya puedes actualizar el número de teléfono de tu Apple ID'),
            ('Incendios en los cerros','Incendios en los cerros'),
        ],
    )
    def test_format_subject(self, subject, expected):

        # Act
        result = format_subject(subject)

        assert result == expected

    def test_format_uid(self):

        # Arrange
        raw_uid = 1

        # Act
        result = format_uid(raw_uid)

        assert result == raw_uid
