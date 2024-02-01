from datetime import datetime

import pytest

from src.sanitize import format_date, format_email, format_subject, format_uid


class TestSanitize:

    email_test_cases = [
        ('Formularios de Google <forms-receipts-noreply@google.com>','forms-receipts-noreply@google.com'),
        ('"Reed.co.uk" <no-reply@jobs.reed.co.uk>','no-reply@jobs.reed.co.uk'),
        ('BrainStation New York | Tech Skills and Careers <info@email.meetup.com>','info@email.meetup.com'),
        ('"Grammarly Premium" <hello@mail.grammarly.com>','hello@mail.grammarly.com'),
        ('Platform Engineers Buenos Aires <info@email.meetup.com>','info@email.meetup.com'),
        ('"Dice Job Alert" <jobs@dice.com>','jobs@dice.com'),
        ('"Computrabajo" <no-reply@computrabajo.com>','no-reply@computrabajo.com'),
        ('TrueUp <hello@trueup.io>','hello@trueup.io'),
        ('Platform Engineers Buenos Aires <info@email.meetup.com>','info@email.meetup.com'),
        ('"culloaiden3@gmail.com" <culloaiden3@gmail.com>','culloaiden3@gmail.com'),
        ('nki.sm.PNCLab <pnclab@nki.rfmh.org>','pnclab@nki.rfmh.org'),
        ('Joe Biden <info@contact.joebiden.com>','info@contact.joebiden.com'),
    ]

    date_test_cases = [        
        ('Tue, 30 Jan 2024 14:57:41 -0800', datetime.fromisoformat('2024-01-30 14:57:41-08:00')),
        ('Wed, 31 Jan 2024 01:34:44 +0000', datetime.fromisoformat('2024-01-31 01:34:44+00:00')),
        ('Wed, 31 Jan 2024 03:04:13 +0000', datetime.fromisoformat('2024-01-31 03:04:13+00:00')),
        ('Wed, 31 Jan 2024 10:08:50 +0000 (UTC)', datetime.fromisoformat('2024-01-31 10:08:50+00:00')),
        ('Wed, 31 Jan 2024 12:19:20 +0000', datetime.fromisoformat('2024-01-31 12:19:20+00:00')),
        ('Wed, 31 Jan 2024 13:11:41 +0000 (UTC)', datetime.fromisoformat('2024-01-31 13:11:41+00:00')),
        ('Wed, 31 Jan 2024 14:33:55 +0000', datetime.fromisoformat('2024-01-31 14:33:55+00:00')),
        ('Wed, 31 Jan 2024 18:19:36 +0000 (UTC)', datetime.fromisoformat('2024-01-31 18:19:36+00:00')),
        ('Wed, 31 Jan 2024 20:38:12 +0000 (UTC)', datetime.fromisoformat('2024-01-31 20:38:12+00:00')),
        ('Wed, 31 Jan 2024 21:10:02 +0000', datetime.fromisoformat('2024-01-31 21:10:02+00:00')),
        ('Wed, 31 Jan 2024 21:25:15 +0000 (UTC)', datetime.fromisoformat('2024-01-31 21:25:15+00:00')),
        ('31 Jan 2024 13:49:22 +0000', datetime.fromisoformat('2024-01-31 13:49:22+00:00')),
    ]

    subject_test_cases = [
        ('=?ISO-8859-1?Q?Ya_puedes_actualizar_el_n=FAme?=\r\n\
        =?ISO-8859-1?Q?ro_de_tel=E9fono_de_tu_Apple=A0ID?=', 'Ya puedes actualizar el número de teléfono de tu Apple ID'),
        ('Time for your appointment!','Time for your appointment!'),
        ('Added today: new Permanent \'Software Developer\' Jobs | Rochester Jobs & Vacancies...','Added today: new Permanent \'Software Developer\' Jobs | Rochester Jobs & Vacancies...'),
        ('[GitHub] Your Dependabot alerts for the week of Jan 23 - Jan 30','[GitHub] Your Dependabot alerts for the week of Jan 23 - Jan 30'),
        ('=?utf-8?B?SGVsbG8sIGdvbGRlbiBnb29kbmVzcyDinKg=?= ','Hello, golden goodness ✨'),
        ('=?utf-8?B?SW50ZWxsaVNlYXJjaOKEoiBBbGVydCBmb3VuZCAxMzUgbmV3IGpv?==?utf-8?B?YnMsIGJhc2VkIG9uIHlvdXIgcHJvZmlsZSA=?=','IntelliSearch™ \
Alert found 135 new jobs, based on your profile '),
        ('Instantly get 3 free months by referring a friend','Instantly get 3 free months by referring a friend'),
        ('=?utf-8?Q?=C3=9ALTIMA=20PREVENTA=20PARA=20CAMDEN?=','ÚLTIMA PREVENTA PARA CAMDEN'),
        ('=?UTF-8?q?4-Unit_Vacation_Rental_in_New_York_=F0=9F=8C=87_26%_Initial_Ren?==?UTF-8?q?tal_Yield_|_Managed_by_Airbnb_Superhost?=','4-Unit Vacation Rental in New York 🌇 26% Initial Rental Yield | Managed by Airbnb Superhost'),
        ('=?ISO-8859-1?Q?Ya_puedes_actualizar_el_n=FAme?==?ISO-8859-1?Q?ro_de_tel=E9fono_de_tu_Apple=A0ID?=','Ya puedes actualizar el número de teléfono de tu Apple ID'),
    ]

    uid_test_cases = [
        (1, 1),
        (10, 10),
        (100, 100),
        (199999, 199999),
    ]
    
    @pytest.mark.parametrize(
        ('email', 'expected'), email_test_cases
    )
    def test_format_email(self, email, expected):

        # Act
        result = format_email(email)

        assert result == expected

    @pytest.mark.parametrize(
        ('date', 'expected'), date_test_cases
    )
    def test_format_date(self, date, expected):

        # Act
        result = format_date(date)

        assert result == expected

    @pytest.mark.parametrize(
        ('subject', 'expected'), subject_test_cases
    )
    def test_format_subject(self, subject, expected):

        # Act
        result = format_subject(subject)

        assert result == expected

    @pytest.mark.parametrize(
        ('uid', 'expected'), uid_test_cases
    )
    def test_format_uid(self, uid, expected):

        # Act
        result = format_uid(uid)

        assert result == expected
