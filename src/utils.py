import json


def read_json(filename: str) -> list[dict]:
    """функция читает json файл. если есть ошибки, то выводит пустой файл"""
    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []
