def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карты по правилу XXXX XX** **** XXXX."""

    if not card_number.isdigit():
        raise ValueError ("В номере карты должны быть только цифры!")
    if len(card_number) != 16:
        raise ValueError ("В номере карты должно быть 16 цифр!")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(card_number: str) -> str:
    """Функция возвращает маску номера счета по правилу **XXXX."""

    if not card_number.isdigit():
        raise ValueError ("В номере счета должны быть только цифры!")
    elif len(card_number) != 20:
        raise ValueError ("В номере счета должно быть 20 цифр!")
    else:
        return f"**{card_number[-4:]}"
