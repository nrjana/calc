import math

def calculator():
    print("выбрать оператион:\n1. плюс(+)\n2. минус (-)\n3. умножить (*)\n4. разделить (/)\n5. процентик (%)\n6. степень(^)\n7. корень (√)")
    
 operation = input("напиши номер опервции; ")
 
 if operation == '7':
     num1 = float(input ("напиши циферку: "))
     print(f"резы: {math.sqrt(num1)}" if num1 >= 0 else "эррор: корень из отриц числа! "   )