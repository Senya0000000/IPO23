import time  # Импорт модуля для работы с временем
from functools import wraps  # Импорт декоратора wraps из модуля functools

def timeit(method):
    """
    Декоратор для измерения времени выполнения функции.

    :param method: Функция, время выполнения которой измеряется.
    :return: Декорированная функция.
    """
    @wraps(method)
    def timed(*args, **kw):
        """
        Функция, замеряющая время выполнения переданной функции.

        :param args: Позиционные аргументы функции.
        :param kw: Именованные аргументы функции.
        :return: Результат выполнения функции.
        """
        ts = time.monotonic()  # Запись текущего времени перед выполнением функции
        result = method(*args, **kw)  # Выполнение функции
        te = time.monotonic()  # Запись времени после выполнения функции
        ms = (te - ts) * 1000  # Вычисление времени выполнения в миллисекундах
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')  # Вывод информации о времени выполнения
        return result
    return timed

# использование:

@timeit
def slow_func(x, y, sleep):
    """
    Функция, имитирующая долгое выполнение с использованием time.sleep.

    :param x: Первый аргумент.
    :param y: Второй аргумент.
    :param sleep: Время задержки в секундах.
    :return: Сумма x и y.
    """
    time.sleep(sleep)
    return x + y

slow_func(10, 20, sleep=2)  # Вызов декорированной функции с замером времени