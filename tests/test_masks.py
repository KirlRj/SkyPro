import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234abcd12345678", ValueError),
        ("12345678", ValueError),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_mask_card_number(card_number)
    else:
        assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("40817810099910004312", "**4312"),
        ("4081781009991000431A", ValueError),
        ("12345", ValueError),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_mask_account(account_number)
    else:
        assert get_mask_account(account_number) == expected
