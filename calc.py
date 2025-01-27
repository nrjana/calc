import math

def calculator():
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Процент (%)")
    print("6. Степень (^)")
    print("7. Корень (√)")

    operation = input("Введите номер операции: ")

    if operation in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

    elif operation == '7':
        num1 = float(input("Введите число для вычисления корня: "))
    
    if operation == '1':
        print(f"Результат: {num1 + num2}")
    elif operation == '2':
        print(f"Результат: {num1 - num2}")
    elif operation == '3':
        print(f"Результат: {num1 * num2}")
    elif operation == '4':
        if num2 != 0:
            print(f"Результат: {num1 / num2}")
        else:
            print("Ошибка: деление на ноль!")
    elif operation == '5':
        print(f"Результат: {(num1 * num2) / 100}")
    elif operation == '6':
        print(f"Результат: {num1 ** num2}")
    elif operation == '7':
        if num1 >= 0:
            print(f"Результат: {math.sqrt(num1)}")
        else:
            print("Ошибка: нельзя извлечь корень из отрицательного числа!")

calculator()
