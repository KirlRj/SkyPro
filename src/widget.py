from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция возвращает маску. Для карты XXXX XX** **** XXXX. Для счета **XXXX"""
    number = card_number[-1]
    name = card_number[:-1]
    if  name.lower().startswith(("счет", "счёт")):
        mask_number = f


