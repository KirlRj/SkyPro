from pathlib import Path

from src.external_api import transfer_currency
from src.find import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_csv, read_excel, read_json
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        num = input()
        if num == "1":
            print("Для обработки выбран JSON-файл.")
            data = read_json(Path("data") / "operations.json")
        elif num == "2":
            print("Для обработки выбран CSV-файл.")
            data = read_csv(Path("data") / "transactions.csv")
        elif num == "3":
            print("Для обработки выбран XLSX-файл.")
            data = read_excel(Path("data") / "transactions_excel.xlsx")
        else:
            continue
        print("Прочитанные данные:", data)
        correct_status = ["EXECUTED", "CANCELED", "PENDING"]
        input_status = None
        while input_status not in correct_status:
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print(f"Доступные для фильтровки статусы: {correct_status}")
            input_status = input()
            if input_status.strip().upper() not in correct_status:
                print(f"Статус операции {input_status} недоступен")
            else:
                input_status = input_status.strip().upper()

        data = filter_by_state(data, input_status)
        print("Прочитанные данные:", data)
        while True:
            print("Отсортировать операции по дате? Да/Нет")
            answer_1 = str(input())
            if answer_1.lower() == "да":
                while True:
                    print("Отсортировать по возрастанию или по убыванию?")
                    answer_2 = str(input())
                    if answer_2.lower() == "по возрастанию":
                        data = sort_by_date(data, True)
                        break
                    elif answer_2.lower() == "по убыванию":
                        data = sort_by_date(data, False)
                        break
                    else:
                        print(f"функции {answer_2} не существует")
                        continue
                break
            elif answer_1.lower() == "нет":
                break
            else:
                print(f"функции {answer_1} не существует")
                continue

        while True:
            print("Выводить только рублевые транзакции? Да/Нет")
            answer_3 = str(input())
            if answer_3.lower() == "да":
                data = list(filter_by_currency(data, "RUB"))
                break
            elif answer_3.lower() == "нет":
                break
            else:
                print(f"функции {answer_3} не существует")
                continue
        print("Прочитанные данные:", data)
        while True:
            print("Отфильтровать список транзакций по определенному слову в описании?")
            answer_4 = str(input())
            if answer_4.lower() == "да":
                print("Введи слово")
                filtered_word = str(input())
                data = process_bank_search(data, filtered_word)
                break
            elif answer_4.lower() == "нет":
                break
            else:
                print(f"функции {answer_4} не существует")
                continue
        print("Прочитанные данные:", data)
        if len(data) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке:{len(data)}")
            for transaction in data:
                date = get_date(transaction["date"])
                description = transaction.get("description", "")
                from_account = mask_account_card(transaction.get("from", ""))
                to_account = mask_account_card(transaction.get("to", ""))
                amount = transfer_currency(transaction)
                currency = transaction.get("currency", "")

                print(f"{date} {description}")
                if from_account:
                    print(f"{from_account} -> {to_account}")
                else:
                    print(f"{to_account}")
                print(f"Сумма: {amount} {currency}")
                print()

        break
