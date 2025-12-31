from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция возвращает маску. Для карты XXXX XX** **** XXXX. Для счета **XXXX"""

    if not card_number or type(card_number) != str or card_number.strip() == "":
        return ""

    info = card_number.split()
    number = info[-1]
    name = " ".join(info[:-1])

    try:
        if name.lower().startswith(("счет", "счёт")):
            if number.isdigit() and len(number) == 20:
                mask_number = get_mask_account(number)
            else:
                mask_number = f"**{number[-4:]}"
        else:
            if number.isdigit() and len(number) == 16:
                mask_number = get_mask_card_number(number)
            else:
                mask_number = number
    except Exception:
        mask_number = number
    return f"{name} {mask_number}".strip()

def get_date(date_str: str) -> str:
    """Функция преобразует дату в формат 'DD.MM.YYYY'"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
