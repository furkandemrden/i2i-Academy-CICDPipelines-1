from app import calculate_telecom_tax


def test_calculate_telecom_tax_valid_amount():
    """
    100 TL base amount with 20% VAT + 7.5% telecom tax
    should result in 127.5 TL final amount.
    """
    assert calculate_telecom_tax(100.0) == 127.5
