sentence = "python is a great programming language"
words = sentence.split()
if len(words) < 2:
     print("too short")
else:
    words[::2]=[word.capitalize() for word in words[::2]]
    print(" ".join(words))
 