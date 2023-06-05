class Student:
    pass

class Marks:
    pass

student1 = Student()
mark1 = Marks()

print(isinstance(student1, Student)) # prints True
print(isinstance(mark1, Marks)) # prints True

print(issubclass(Student, object)) # prints True
print(issubclass(Marks, object)) # prints True