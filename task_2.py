# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

while True:
    # Ввод числа
    number = int(input("Введите число от 1 до 100000: "))

    # Проверка ограничений на ввод
    if number < 0 or number > 100000:
        print("Число должно быть положительным и не превышать 100000")
        continue
    else:
        is_prime = True
        if number <= 1:
            is_prime = False
        else:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
        # Вывод результата
        if is_prime:
            print("Число является простым")
        else:
            print("Число является составным")
        break