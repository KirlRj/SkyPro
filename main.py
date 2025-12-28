from src.utils import read_csv, read_excel, read_json


def get_status() -> str:
    status = ["EXECUTED", "CANCELED", "PENDING"]
    input_status = None
    while input_status not in status:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {status}")
        input_status = input().strip().upper()
    return input_status


if __name__ == "__main__":
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        num = int(input())
        if num == 1:
            print("Для обработки выбран JSON-файл.")
        elif num == 2:
            print("Для обработки выбран CSV-файл.")
        elif num == 3:
            print("Для обработки выбран XLSX-файл.")
        else:
            continue
