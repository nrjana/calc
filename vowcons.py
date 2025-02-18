words=(input("Введите слово: "))
vowels=0
consonats=0
letters1 = "aeiou"

for word in words:
    if letters1 in words:
        vowels +=1
    else:
        consonats +=1
print(vowels)
print(consonats)