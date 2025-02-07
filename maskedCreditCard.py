card_number = input("ввести номер карты: ")
if len(card_number) == 16:
    print(len(card_number))
    print("*" * 12 + card_number[-4:])

else:
     print("error")
     