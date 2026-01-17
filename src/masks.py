import logging
from pathlib import Path

masks_logger = logging.getLogger(__name__)
masks_logger.setLevel(logging.DEBUG)
masks_handler = logging.FileHandler(Path("src") / "log.txt", mode="w", encoding="utf-8")
masks_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
masks_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты по правилу XXXX XX** **** XXXX."""
    masks_logger.info("Запуск функции get_mask_card_number")
    if not card_number.isdigit():
        masks_logger.error("В номере карты должны быть только цифры!")
        raise ValueError("В номере карты должны быть только цифры!")
    if len(card_number) != 16:
        masks_logger.error("В номере карты должно быть 16 цифр!")
        raise ValueError("В номере карты должно быть 16 цифр!")
    masks_logger.info("Функция get_mask_card_number выполнена успешно ")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str) -> str:
    """Функция возвращает маску номера счета по правилу **XXXX."""
    masks_logger.info("Запуск функции get_mask_account")
    if not card_number.isdigit():
        masks_logger.error("В номере счета должны быть только цифры!")
        raise ValueError("В номере счета должны быть только цифры!")
    elif len(card_number) != 20:
        masks_logger.error("В номере счета должно быть 20 цифр!")
        raise ValueError("В номере счета должно быть 20 цифр!")
    else:
        masks_logger.info("Функция get_mask_account выполнена успешно ")
        return f"**{card_number[-4:]}"
