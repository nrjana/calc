salary = float(input("напишите вашу зп:  "))
rating = float(input("напишите ваш кредитный рейтинг: "))

if salary > 50000:
    if rating > 700:
        print("кредит одобрен с низким процентом.")
    else:
        print("кредит одобрен, но с высоким процентом.")

else:
    if rating > 700:
        print("кредит одбрен, но со строгими условмями.")
    else:
        print("кредит не одобрен....")

        