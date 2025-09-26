
# def sum(a, b):
    # return a + b

# def multiply(a, b):
#     return a * b

# def sum(a, b, *args):
#     sum = a + b
#     print(a, b)
#     for item in args:
#         sum = sum + item
#     return sum


# a = 5
# b = 10
# # print(sum(a, b), multiply(a, b))

# d = {
#     "a": 5,
#     "b": 10
# }
# # print(multiply(**d))
# print(sum(1, 2, 3, 4, 5))

# x = 5
# x = 4
# #..
# x = 1

# def func(x):
#     if x == 0:
#         return 
#     print(f"before {x}")
#     func(x - 1)
#     print(f"after {x}")
#     # print(x)

# func(5)

d = {
    "a": 5,
    "b": 1000,
}
c = "asdfasdf"


# class Student():
#     name = None
#     surname = None
#     gpa = None

#     def __init__(self, name, surname, gpa):
#         self.name = name
#         self.surname = surname
#         self.gpa = gpa

#     # def print(self):
#         # print(self.name, self.surname, self.gpa)

#     def __str__(self):
#         return f"Name: {self.name}, Surname: {self.surname}, gpa: {self.gpa}"

    


# student = Student("Azamat", "Azamatovich", 4)

# # student.__init__("Hello", "Wrold", 3)

# # print(student)

# class Human():
#     name = None
#     surname = None

#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     # def print(self):
#         # print(self.name, self.surname, self.gpa)

#     def __str__(self):
#         return f"Name: {self.name}, Surname: {self.surname}"


# class Student(Human):
#     gpa = None
    
#     def __init__(self, name, surname, gpa):
#         super().__init__(name, surname)
#         self.gpa = gpa
    
#     def __str__(self):
#         human = super().__str__()
#         return f"{human}, gpa: {self.gpa}"
#         # return f"Name: {self.name}, Surname: {self.surname}"


# class Teacher(Human):
#     students = 0
    
#     def __init__(self, name, surname, students):
#         super().__init__(name, surname)
#         self.students = students

#     def __str__(self):
#         human = super().__str__()
#         return f"{human}, students count: {self.students}"
#         # return f"Name: {self.name}, Surname: {self.surname}"

# student = Student("Azamat", "Azamatovich", 4)
# teacher = Teacher("Aibolat", "Azamatovich", 30)

# # print(student)
# print(teacher.name)
# print(student.gpa)

x = lambda a, b : a * b
print(x(5, 10))