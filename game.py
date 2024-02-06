import numpy as np

def binary_search_guess_number():
    low = 1
    high = 100
    attempts = 0

    user_number = int(input("Загадайте число от 1 до 100: "))

    while low <= high:
        mid = (low + high) // 2
        print(f"Это число {mid}?")
        attempts += 1

        user_input = input("Введите 'больше', 'меньше' или 'да': ").strip().lower()

        if user_input == 'да':
            print(f"Угадал за {attempts} попыток!")
            break
        elif user_input == 'больше':
            low = mid + 1
        elif user_input == 'меньше':
            high = mid - 1
        else:
            print("Пожалуйста, введите 'больше', 'меньше' или 'да'.")

if __name__ == "__main__":
    binary_search_guess_number()






