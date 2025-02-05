membership = input("ввести тип членства: ")
amount = float(input("ввести сумму покупки: "))

if membership == "золото":
    if amount > 100:
        discount = 0.2
    else:
        discount = 0.1

elif membership == "серебро":
     if amount > 100:
        discount = 0.15
     else:
        discount = 0.05
else:
    if amount > 100:
        discount = 0.05
    else:
        discount = 0

total_price = amount * (1- discount)
print(f"сумма после скидки: {total_price:.2f}")
