# Импорт библиотек
from datetime import datetime
from functools import wraps
from time import time

from src.masks import get_mask_card_number


# декоратор логов
def log(filename=None):

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            time_start = time()
            start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            start_data_log = f"Передаваемые данные в функцию {function.__name__}: {args}, {kwargs}"
            start_time_log = f"Начало выполнения функции {function.__name__} - {start}"

            result = function(*args, **kwargs)

            time_end = time()
            end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end_time_log = f"Окончание выполнения функции {function.__name__} - {end}"
            end_data_log = f"Результат выполнения функции {function.__name__}: {result}"
            time_function = f"Выполнение функции заняло {time_end - time_start:.7f} секунд"

            logs = "\n".join([start_data_log, start_time_log, end_time_log, time_function, end_data_log])

            if filename:
                with open(filename, "a") as f:
                    f.write(logs + "\n")
            else:
                print(logs)

            return result

        return wrapper

    return decorator


@log()
def mask_card_number(card_number: str) -> str:
    return get_mask_card_number(card_number=card_number)


print(mask_card_number("1234561234561313"))
