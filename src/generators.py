from typing import Any


def filter_by_currency(transactions: list, currency: str) -> Any:
    """Функция, возвращающая по очереди транзакции, по ключу currency"""

    for transaction in transactions:
        file_currency = transaction.get("currency_code")
        json_currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

        if file_currency == currency or json_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Any:
    """Функция, возвращающая описание операции"""
    for transaction in transactions:
        yield transaction.get("description", {})


def card_number_generator(start: int, end: int) -> Any:
    """Функция, генерирующая номера карт по порядку"""
    if len(str(start)) > 16 or len(str(end)) > 16:
        raise ValueError("Номер карты больше 16 цифр!")
    else:
        for number in range(start, end + 1):
            numcard = str(number).zfill(16)
            yield " ".join(numcard[i : i + 4] for i in range(0, len(numcard), 4))
