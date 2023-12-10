class Student:
    def __init__(self, new_name, new_grades) -> None:
        self.name = new_name
        self.grades = new_grades
    
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def __avg__(self):
        return self.average()
    

    def __len__(self):
        return len(self.grades)


    def __getitem__(self, i) -> float:
        return self.grades[i]
    

    def __repr__(self) -> str:
        return f'<Student {self.grades}>'
    

    def __str__(self) -> str:
        return f'Student with {len(self)} grades'
    

    def add_grade(self, newgrade: float):
        self.grades.append(newgrade)




student =  Student("mr Anderson", [10,20,30,40,50,60])

print(student.name)
print(Student.average(student))
print(student.__class__)
print(student[2])
print(student)