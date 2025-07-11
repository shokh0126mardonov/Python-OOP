class Student:
    def __init__(self,name: str,age: int,grade: int):
        self.grade = grade
        self.age = age
        self.name = name
        
    def info(self):
        print(f"{self.name},{self.age} yoshda, {self.grade}- sinf o'quvchisi")
        return
    
student01 = Student("Shohjahon",19,2)
student02 = Student("Bexrux",20,2)
student01.info()