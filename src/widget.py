from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция возвращает маску. Для карты XXXX XX** **** XXXX. Для счета **XXXX"""
    info = card_number.split()
    number = info[-1]
    name = " ".join(info[:-1])

    if  name.lower().startswith(("счет", "счёт")):
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)
    return f"{name} {mask_number}"


def get_date(data: str) -> str:
    """Функиця возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"