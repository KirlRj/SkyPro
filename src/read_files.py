import csv
from typing import Any, Dict, List

import pandas as pd


def read_csv(path_file: str) -> List[Dict[str, str]]:
    """Функция чтения csv файла"""
    with open(path_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        return list(reader)


def read_excel(path_file: str, sheet_name: int = 0) -> List[Dict[Any, Any]]:
    """Функция чтения excel файла"""
    df = pd.read_excel(path_file, sheet_name=sheet_name)
    return df.to_dict(orient="records")
