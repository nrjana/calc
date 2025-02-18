student_mark=[65,90,45,80,50,56,88,92,59,30]
results= []
for marks in student_mark:
    if marks >=60:
        results.append((marks,"pass"))
    else:
        results.append((marks,"fail"))

for result in results:
    print("Marks",result[0], "->", result)