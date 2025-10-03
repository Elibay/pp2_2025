# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# a = ("Apple", "Juice", "Pen", "Peach")
# # (), [], {}, set

# # __iter__
# # next
# i = iter(a)
# # for i in a:
# #     print(i)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

def to_upper(func):
    def inner_function():
        return func().upper()
    return inner_function

@to_upper
def hello():
    return "Hello world"
    
@to_upper
def print_name():
    return "Hello Aza!"

print(hello())
print(print_name())


import math
def multipy_by_two(func):
    def inner_function():
        return 2 * func()
    return inner_function
    
def find_c(func):
    def inner_function(x, y):
        a, b = func(x, y)
        c = math.sqrt(a * a + b * b)
        return c
    return inner_function

def find_p(func):
    def inner_function(a, b):
        c = func(a, b)
        return a + b + c
    return inner_function

# math.pi
# pow
# sqrt

@find_p
@find_c    
def result(a, b):
    # a = 5
    # b = 10
    return a, b

print(result(5, 10))

import datetime

x = datetime.datetime.now()
print(x)






