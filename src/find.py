import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(transactions: List[Dict[str, Any]], search: str) -> list[dict]:
    """функция вывода списка словарей по ключевому слову."""
    pattern = re.compile(search, re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)

    return result


def count_bank_operations(transactions: List[Dict[Any, Any]]) -> Counter[Any]:
    """функция подсчета операций по категориям"""
    data = []

    for transaction in transactions:
        description = transaction.get("description")
        if description:
            data.append(description)

    return Counter(data)
