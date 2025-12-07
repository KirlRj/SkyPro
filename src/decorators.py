# Импорт библиотек
from datetime import datetime
from functools import wraps
from time import time
from typing import Any, Callable, Optional

# декоратор логов
def log(filename: Optional[str] = None) -> Callable:

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            error = None
            time_start = time()
            start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chapter = "=" * 100
            start_data_log = f"Передаваемые данные в функцию {function.__name__}: {args}, {kwargs}"
            start_time_log = f"Начало выполнения функции {function.__name__} - {start}"

            try:
                result = function(*args, **kwargs)
                status = f"Функция {function.__name__} выполнена 'Успешно'!"
                end_data_log = f"Результат выполнения функции {function.__name__}: {result}"
            except Exception as e:
                result = None
                error = e
                status = f"Ошибка выполнения функции! Ошибка: {e}"
                end_data_log = "Функция завершилась с ошибкой. Результаты не получены."

            time_end = time()
            end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end_time_log = f"Окончание выполнения функции {function.__name__} - {end}"
            time_function = f"Выполнение функции заняло {time_end - time_start:.7f} секунд"

            logs = "\n".join(
                [chapter, start_data_log, start_time_log, end_time_log, time_function, status, end_data_log, chapter]
            )

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(logs + "\n")
            else:
                print(logs)

            if error:
                raise error

            return result

        return wrapper

    return decorator
