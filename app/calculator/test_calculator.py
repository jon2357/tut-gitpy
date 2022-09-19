# python -m pytest -v --cov

import pytest
from .calculator import add_numbers

#### Test for supported values in add_numbers ####

# Test max_loan_amount
testdata = [
    ([3, 4], 7),
    ([3, -4], -1),
    ([-3, 4], 1),
    ([5, 0.5], 5.5),
    ([4, 3, 3], 10),
    ([37], 37),
]


@pytest.mark.parametrize("number_addition_list,expected_value", testdata)
def test_add_numbers(number_addition_list, expected_value):
    value = add_numbers(number_addition_list)
    assert value == expected_value


#### Test for unsupported values in add_numbers ####
def test_add_numbers_raises_int_not_iterable():
    with pytest.raises(Exception) as exc_info:
        value = add_numbers(37)
    assert "'int' object is not iterable" in str(exc_info.value)


unsupported_testdata = ["ert", "[34, 45]", ["34", "45"], ["w", "e"]]


@pytest.mark.parametrize("input_value", unsupported_testdata)
def test_add_numbers_raises_unsupported_input(input_value):
    with pytest.raises(Exception) as exc_info:
        value = add_numbers(input_value)
    assert "unsupported operand type(s)" in str(exc_info.value)
