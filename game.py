import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def benchmark_algorithm(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_list = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_numbers = np.random.randint(1, 101, size=1000)  # генерируем список случайных чисел

    for number in random_numbers:
        count_list.append(random_predict(number))

    average_attempts = int(np.mean(count_list))
    print(f"Ваш алгоритм угадывает число в среднем за {average_attempts} попыток")
    return average_attempts

if __name__ == "__main__":
    # Запуск функции
    benchmark_algorithm(random_predict)

