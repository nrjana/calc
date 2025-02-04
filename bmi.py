height = float(input("ввести рост: "))
weight = float(input("ввести вес: "))

height_m = height / 100
bmi = weight / (height_m * height_m)

print("твой индекс массы тела:", bmi)

if bmi < 18.5:
    print("недостаток веса")
elif bmi < 24.9:
    print("классный вес")
elif bmi < 29.9:
    print("много веса")
elif bmi < 34.9:
    print("ой ожирение 1 уровень")
elif bmi < 39.9:
    print("ой ожирение 2 уровень") 
else:
    print("запущенное ожирение 3 уровень")  
    
    