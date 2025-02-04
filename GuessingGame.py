import random

number = random.randint(1,100)
while True:
    guess = int(input("угадай число от 1 до 100!!"))
    if guess == number:
        print("йоо угадал!")
        break
    elif abs(guess - number) > 10:
        print("горячо")
    else:
        print("холодно")
        