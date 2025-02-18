numbers = [22,45,67,12,89,34,55,90,10]
largest = numbers [0]
smallest = numbers [0]
 
for numbers in numbers:
    if numbers > largest:
        largest = numbers
    if numbers < smallest:
        smallest = numbers

print(largest)   
print(smallest)