from typing import Any, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def all_transactions() -> Any:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 583920475,
            "state": "CANCELED",
            "date": "2019-01-15T14:12:30.123456",
            "operationAmount": {"amount": "4500.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Оплата поставщику",
            "from": "Счет 23456789012345678901",
            "to": "Счет 10987654321098765432",
        },
        {
            "id": 726354890,
            "state": "EXECUTED",
            "date": "2020-07-20T10:45:12.654321",
            "operationAmount": {"amount": "12000.50", "currency": {"name": "JPY", "code": "JPY"}},
            "description": "Перевод на карту",
            "from": "Счет 34567890123456789012",
            "to": "Счет 21098765432109876543",
        },
        {
            "id": 834756291,
            "state": "EXECUTED",
            "date": "2021-03-11T08:30:00.000000",
            "operationAmount": {"amount": "6500.75", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод зарплаты",
            "from": "Счет 45678901234567890123",
            "to": "Счет 32109876543210987654",
        },
    ]


def test_filter_by_currency_usd(all_transactions: List[dict]) -> None:
    result = list(filter_by_currency(all_transactions, "USD"))
    assert len(result) == 3


def test_filter_by_currency_empty(all_transactions: List[dict]) -> None:
    result = list(filter_by_currency(all_transactions, " "))
    assert len(result) == 0


def test_transaction_descriptions(all_transactions: List[dict]) -> None:
    result = list(transaction_descriptions(all_transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата поставщику",
        "Перевод на карту",
        "Перевод зарплаты",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (2, 5, ["0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator_range(start: int, stop: int, expected: List[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected


@pytest.mark.parametrize(
    "start, stop",
    [
        (10**16, 1),
        (1, 10**16),
    ],
)


def test_card_number_generator_too_long(start: int, stop: int) -> None:
    with pytest.raises(ValueError, match="Номер карты больше 16 цифр!"):
        list(card_number_generator(10**16, 1))
