from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(dict_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащие ключ state == входному значению"""
    filtered_list = []
    for item in dict_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(dict_list: List[Dict[str, Any]], sort: bool = True) -> List[Dict[str, Any]]:
    sorted_list = sorted(dict_list, key=lambda item: datetime.fromisoformat(item["date"]), reverse=sort)
    return sorted_list
