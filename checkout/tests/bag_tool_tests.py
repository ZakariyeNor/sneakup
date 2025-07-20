import pytest
from decimal import Decimal
from yourapp.templatetags.your_template_file import calc_subtotal, multiply_vat

def test_calc_subtotal():
    # Test with integers
    assert calc_subtotal(10, 3) == 30
    # Test with floats
    assert calc_subtotal(9.99, 2) == 19.98
    # Test with Decimal
    assert calc_subtotal(Decimal('5.5'), 4) == Decimal('22.0')
    # Test with zero quantity
    assert calc_subtotal(10, 0) == 0

def test_multiply_vat():
    # Test normal multiplication with float args
    assert multiply_vat(100, 0.06) == 6.0
    # Test normal multiplication with Decimal args
    assert multiply_vat(Decimal('50.0'), Decimal('0.2')) == 10.0
    # Test with string numeric inputs
    assert multiply_vat('100', '0.15') == 15.0
    # Test invalid inputs return empty string
    assert multiply_vat('abc', 0.06) == ''
    assert multiply_vat(100, 'xyz') == ''
    assert multiply_vat(None, 0.1) == ''
