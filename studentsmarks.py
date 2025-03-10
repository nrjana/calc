students = [
    {
        "name": "Alice",
        "subjects": ("Math", "Physics", "English"),
        "scores": {"Math": 85, "Physics": 78, "English": 92}},
    {
        "name": "Bob",
        "subjects": ("Math", "Biology", "English"),
        "scores": {"Math": 72, "Biology": 88, "English": 80}},
    {"name": "Charlie",
        "subjects": ("Math", "Physics", "Chemistry"),
        "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]


#1
def display_students(data):
    for student in data:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f"{name} is enrolled in: {subjects}")

display_students(students)



#2
def get_average_score(name, data):
    for student in data:
        if student['name'] == name:
            scores = student['scores'].values()
            if len(scores)>0:
                return sum (scores)/ len(scores)
            
print(get_average_score("Bob", students))




#3
def find_top_student(students):
    top_student=""
    highest_average=0
    for student in students:
        scores = student['scores'].values()
        if len(scores)>0:
            average_score= sum (scores)/ len(scores)
            if average_score>highest_average:
                highest_average=average_score
                top_student=student['name']
    return top_student
print(find_top_student(students))






#4
def failed_students(data, passing_scores=50):
    failed = []
    
    for student in data:
         for score in student["scores"].values():
              if score < passing_scores:
                failed.append((student["name"], score))
                break
    return failed           
       

print(failed_students(students, passing_scores=75))





#bonus
def unique_subjects(students):
    subjects = set()
    for student in students:
        subjects.update(student ["subjects"])
        return subjects

print(unique_subjects(students))