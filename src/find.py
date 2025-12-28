import re
from collections import Counter

def process_bank_search(transactions: list[dict], search: str) -> list[dict]:
    """функция вывода списка словарей по ключевому слову."""
    pattern = re.compile(search, re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)

    return result
