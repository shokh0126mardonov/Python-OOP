class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Ism:{self.name} yosh:{self.age}")

student1 = Student("Ali", 20)
student2 = Student("Vali", 23)
student3 = Student("Laylo", 22)
student4 = Student("Diyor", 25)
student5 = Student("Madina", 21)

student = [student1,student2,student3,student4,student5]

result = max(student,key=lambda age:age.age)

result.show_info()