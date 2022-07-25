import pytest
from main import get_emails, get_phone_numbers


# @pytest.mark.skip('get email')
def test_get_email():
    text = 'email.text'
    actual = get_emails(text)
    expected = 'Brendonhampton1988@gmail.com'
    assert actual == expected


# @pytest.mark.skip('get phone number')
def test_get_phone_number():
    text = 'phone.text'
    actual = get_phone_numbers(text)
    expected = '088-927-9985'
    assert actual[0] == expected
