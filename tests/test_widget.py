import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected_mask",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
    ],
)
def test_mask_account_card(input_str: str, expected_mask) -> None:
    result = mask_account_card(input_str)
    assert result == expected_mask


@pytest.mark.parametrize(
    "input_date, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_date(input_date: str, expected_date: str) -> None:
    assert get_date(input_date) == expected_date
