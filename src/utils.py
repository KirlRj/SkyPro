import json


def read_json(filename: str) -> list[dict]:
    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []
