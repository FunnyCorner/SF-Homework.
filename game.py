import numpy as np

def random_guess_number():
    # Генерируем случайный массив чисел от 1 до 100 и сортируем его
    a = np.sort(np.random.randint(1, 101, size=10))
    print(a)

    value = int(input("Загадайте число от 1 до 100: "))

    attempts = 0
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Это число {a[mid]}?")
        attempts += 1

        if value == a[mid]:
            print(f"Угадал за {attempts} попыток!")
            break
        elif value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("Число не найдено.")

if __name__ == "__main__":
    random_guess_number()






