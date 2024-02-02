import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # Инициализируем счетчик попыток
    low_limit, high_limit = 1, 100  # Устанавливаем начальные границы поиска
    
    while low_limit <= high_limit:
        mid = (low_limit + high_limit) // 2  # Находим среднее значение
        count += 1  # Увеличиваем счетчик попыток

        if mid == number:
            return count  # Если угадали число, возвращаем количество попыток
        elif mid < number:
            low_limit = mid + 1  # Если загаданное число больше, обновляем нижнюю границу
        else:
            high_limit = mid - 1  # Если загаданное число меньше, обновляем верхнюю границу
    
    return count  # Возвращаем количество попыток при неудаче