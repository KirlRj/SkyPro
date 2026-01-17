import csv
import json
import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

log_path = Path("src") / "log.txt"
utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
utils_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)


def read_json(filename: Path | str) -> list[dict]:
    """функция читает json файл. если есть ошибки, то выводит пустой файл"""
    utils_logger.info("запуск функции read_json ")
    try:

        with open(filename, encoding="utf-8") as f:
            utils_logger.info(f"чтение json файла {filename}")
            data = json.load(f)

        if not isinstance(data, list):
            utils_logger.error("неверный тип данных файла json!")
            return []

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        utils_logger.error("файл не найден!")
        return []


def read_csv(path_file: Path | str) -> List[Dict[str, str]]:
    """Функция чтения csv файла"""
    with open(path_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def read_excel(path_file: Path | str, sheet_name: int = 0) -> List[Dict[Any, Any]]:
    """Функция чтения excel файла"""
    df = pd.read_excel(path_file, sheet_name=sheet_name)
    return df.to_dict(orient="records")
