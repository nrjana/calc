words = ["apple", "banana", "cherry", "blueberry"]
longest_word = words[0]
for word in words[1:]:
    if len(word) >len(longest_word):    
      longest_word = word
print (f"the longest word is {longest_word}")