score = int(input("введите оценку за тест: "))

if score > 90:
    homework = input("вы сдали всю домашку? (да/нет): ")
    if homework == "да":
        print("замечательно! ваша оценка А+")
    else:
        print("хорошая работта, но сдайте всю домашку! оценка А")

elif score > 80:
    attendance = input("вы посещали 70% занятий? (да/нет)")
    if attendance == "да":
        print("классно! оценка B")
    else:
        print("а надо приходить на занятия!! оценка С")
else:
    print("страйтесь ещё лучше")
