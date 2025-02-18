number = [12,7,34,23,45,66,89,90,41,55]
even=[0]
odd=[0]
for i in number:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("четные числа: ")
print(even)
print("нечетные числа:")
print(odd)