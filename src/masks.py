def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера по правилу XXXX XX** **** XXXX."""

    if len(card_number) != 16:
        return "Введено неверное количество символов в номере карты!"
    elif not card_number.isdigit():
        return "В номере карты есть буквы!"
    else:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(card_number: str) -> str:
    """Функция возвращает маску номера по правилу **XXXX."""

    if len(card_number) != 16:
        return "Введено неверное количество символов в номере карты!"
    elif not card_number.isdigit():
        return "В номере карты есть буквы!"
    else:
        return f"**{card_number[12:]}"
