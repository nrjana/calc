words = ["banana", "apple", "cherry", "grape"] 
letter = "w"
for word in words:
    if letter in word:
        print(word)
    else:
        print("no words found")