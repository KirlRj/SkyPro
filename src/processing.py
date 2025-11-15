from typing import Any, Dict, List


def filter_by_state(dict_list: List[Dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, int]]:
    """Функция возвращает новый список словарей, содержащие ключ state == входному значению"""
    filtered_list = []
    for item in dict_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list

