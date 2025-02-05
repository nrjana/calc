num = int(input("введи число: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("число делится на 4")
    else:
        print("чётное число")

else:
    if num % 5 == 0:
        print("число делится на 5")
    else:
        print("нечётное чиисло")