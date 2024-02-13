def guess_number(secret_number):
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1

        # Загаданное число угадано
        if mid == secret_number:
            return attempts
        
        # Если загаданное число больше предполагаемого
        elif mid < secret_number:
            low = mid + 1
        
        # Если загаданное число меньше предполагаемого
        else:
            high = mid - 1

# Пользователь загадывает число
secret_number = int(input("Пожалуйста, загадайте число от 1 до 100: "))

# Пытаемся угадать число
attempts = guess_number(secret_number)

# Выводим результат
print(f"Компьютер угадал число {secret_number} за {attempts} попыток.")





