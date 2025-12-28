import re
from collections import Counter
from typing import Any, Dict, List

import pytest

from src.find import count_bank_operations, process_bank_search

transactions: List[Dict[Any, Any]] = [
    {"description": "Перевод с карты на счет", "amount": 1000},
    {"description": "Покупка в магазине", "amount": 500},
    {"description": "Перевод наличными", "amount": 2000},
    {"description": "Оплата счета", "amount": 800},
    {"amount": 300},
]


def test_process_bank_search_basic() -> None:
    result = process_bank_search(transactions, "перевод")
    assert len(result) == 2
    for item in result:
        assert "перевод" in item.get("description", "").lower()


def test_process_bank_search_case_insensitive() -> None:
    result = process_bank_search(transactions, "Покупка")
    assert len(result) == 1
    assert result[0]["description"] == "Покупка в магазине"


def test_process_bank_search_no_matches() -> None:

    result = process_bank_search(transactions, "интернет")
    assert result == []


def test_process_bank_search_missing_description() -> None:

    result = process_bank_search(transactions, "счет")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод с карты на счет"


def test_count_bank_operations_basic() -> None:
    result = count_bank_operations(transactions)
    assert isinstance(result, Counter)
    assert result["Перевод с карты на счет"] == 1
    assert result["Покупка в магазине"] == 1
    assert result["Перевод наличными"] == 1
    assert result["Оплата счета"] == 1
    assert None not in result
    assert "" not in result


def test_count_bank_operations_empty_list() -> None:
    result = count_bank_operations([])
    assert result == Counter()


def test_count_bank_operations_single_entry() -> None:
    result = count_bank_operations([{"description": "Оплата услуг"}])
    assert result == Counter({"Оплата услуг": 1})


def test_count_bank_operations_all_none() -> None:
    data: List[Dict[Any, Any]] = [{"amount": 100}, {"description": None}, {"description": ""}]
    result = count_bank_operations(data)
    assert result == Counter()
