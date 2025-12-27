import csv
from typing import Dict, List


def read_csv(path_file: str) -> List[Dict]:
    """Функция чтения csv файла"""
    with open(path_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        return list(reader)