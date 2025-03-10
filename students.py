class Student:
    def _init_(self,name,student_id,grades):
        self.name=name
        self.student_id=student_id
        self.grades=[]

    def add_grade(self,grades):
        self.grades.append(grades)

    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
    
    def get_best_grade(self):
        if not self.grades:
            return None
        return max(self.grades)

    def get_worst_grade(self):
         if not self.grades:
            return None
         return min(self.grades)
          
    def display_info(self):
        average=self.calculate_average()
        print(f"student name : {self.name}")
        print(f"student_id : {self.student_id}")
        print(f"average grades :{average}")
        print(f"best grades :{self.get_best_grade()}")
        print(f"worst grades :{self.get_worst_grade()}")

class StudentManager:
     def _init_(self):
         self.students=[]  

     def add_student(self, student):
         self.students.append(student)

     def display_all_students(self):
         for student in self.students:
             student.display_info()

     def get_top_student(self):   
         top_student=max(self.students,key=lambda student: student.calculate_average())
         return top_student

     def get_lowest_student(self):
         lowest_student=min(self.students,key=lambda student: student.calculate_average())
         return lowest_student


student=Student("steve",101,99)
student.add_grade(80)
student.add_grade(49)
student.add_grade(98)

student1=Student("mark",77,91)
student1.add_grade(83)
student1.add_grade(78)
student1.add_grade(89)

student2=Student("alex",98,89)
student2.add_grade(91)
student2.add_grade(89)
student2.add_grade(79)

manager=StudentManager()

manager.add_student(student)
manager.add_student(student1)
manager.add_student(student2)

print("information about all students")
manager.display_all_students()

top_student=manager.get_top_student()
print("best student: ")
top_student.display_info()

lowest_student=manager.get_lowest_student()
print("worst student: ")
lowest_student.display_info()