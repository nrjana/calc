def calculate_discount(membership_type, purchase_amount):
    if membership_type == "gold":
         if purchase_amount > 100:
            discount = 0.20
         else:
            discount = 0.10

    elif membership_type == "silver":
         if purchase_amount > 100:
            discount = 0.10
         else:
            discount = 0.05

    elif membership_type == "standart":
         if purchase_amount > 100:
            discount = 0.05
         else:
            discount = 0

    else:
         return "что-то пошло не так"
         
    discount_amount = purchase_amount * discount
    final_price = purchase_amount - discount_amount
    return discount_amont, final_price

membership_type = input("напиши тип подписки: ").lower()
purchase_amount = float(input("сумма покупки:  "))

discount_amount, final_price = calculate_discount(membership_type< purchase_amount)
if isinstance(discount_amount, str):
    print(discount_amount)

else:
    print(f"скидка: {discount_amount:.2f}сом")
    print(f"итоговая сумма: {final_price:.2f}сом")