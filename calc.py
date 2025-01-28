import math

def calculator():
    print("выбрать оператион:\n1. плюс(+)\n2. минус (-)\n3. умножить (*)\n4. разделить (/)\n5. процентик (%)\n6. степень(^)\n7. корень (√)")
    
operation = input("напиши номер опервции; ")
 
if operation == '7':
     num1 = float(input ("напиши циферку: "))
     print(f"резы: {math.sqrt(num1)}" if num1 >= 0 else "эррор: корень из отриц числа!")
else:
   num1 = float(input("напиши первое число: "))
   num2 = float(input("напиши второе число: "))

if operation == '1':
   print(f"результат: {num1 + num2}")
elif operation == '2':
   print(f"результат: {num1 - num2}")
elif operation == '3':
   print(f"результат: {num1 * num2}")
elif operation == '4':
   print(f"результат: {num1 / num2 if num2 != 0 else 'ошибка: делить на ноль нельзя пабо!!!'}")

elif operation == '5':
   print(f"результат: {(num1 * num2) / 100}")

elif operation == '6':
   print(f"результат: {num1 ** num2}")

calculator()