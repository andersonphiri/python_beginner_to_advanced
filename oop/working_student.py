import student 

class WorkingStudent(student.Student):
    def __init__(self, name, grades, salary):
        super().__init__(name, grades)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return 40 * self.salary
    
    def __str__(self) -> str:
        return f'{super().__str__()} with a daily salary of {self.salary}'

    @property 
    def weekly_salary_str(self):
        return f'{(40*self.salary):.5f}'

    @classmethod
    def hi(cls):
        print(cls.__name__)
    

    @classmethod
    def from_details(cls, name, grades, salary):
        return cls(name,grades, salary)
    
    # use a static method on es that you are not going to inherit from
    # a static method is equivalent to a class method but with limited functionality
    @staticmethod
    def hello():
        print('yes I am static method')
    


working_student = WorkingStudent("andy", [40,50,60,70], 350)
working_student_two = WorkingStudent.from_details("anderson", [1,2,3,4,5], 400)
print(working_student.weekly_salary)
print(working_student.weekly_salary_str)
working_student.hello()
WorkingStudent.hello()

print('\n\n')
print(working_student_two)