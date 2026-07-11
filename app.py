"""
Simple telecom tax calculator.

Turkey applies a communication/telecom tax on top of the standard VAT for
telecom services. This function takes the base (pre-tax) amount and
returns the final amount the customer pays after both taxes are added.
"""

VAT_RATE = 0.20          # standard VAT
TELECOM_TAX_RATE = 0.075  # special communication (telecom) tax


def calculate_telecom_tax(base_amount: float) -> float:
    """
    Calculate the final payable amount for a telecom service.

    :param base_amount: the pre-tax price of the service (must be >= 0)
    :return: final amount after VAT + telecom tax, rounded to 2 decimals
    :raises ValueError: if base_amount is negative
    """
    if base_amount < 0:
        raise ValueError("base_amount cannot be negative")

    total_tax_rate = VAT_RATE + TELECOM_TAX_RATE
    final_amount = base_amount * (1 + total_tax_rate)
    return round(final_amount, 2)


if __name__ == "__main__":
    price = 100.0
    print(f"Base amount: {price} -> Final amount: {calculate_telecom_tax(price)}")
