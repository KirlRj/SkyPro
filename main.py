from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number("1234567890111342"))
print(get_mask_account("12345678901113421234"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Счет 73654108430135871342"))
print(get_date("2024-03-11T02:26:18.671407"))