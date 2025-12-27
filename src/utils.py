import json
import logging

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
utils_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)


def read_json(filename: str) -> list[dict]:
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
