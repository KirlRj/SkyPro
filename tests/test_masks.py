import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234abcd12345678", "В номере карты должны быть только цифры!"),
        ("12345678", "В номере карты должно быть 16 цифр!"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("40817810099910004312", "**4312"),
        ("4081781009991000431A", "В номере счета должны быть только цифры!"),
        ("12345", "В номере счета должно быть 20 цифр!"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
