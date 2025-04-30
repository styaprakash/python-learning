# def greet(name):
#     print("Hello,",name)
# greet("Satya")
# print(greet)
# def add(a,b):
#     return a+b
# result = add(5,3)
# print("Sum is: ", result)
from itertools import count

# def greet(name="friend"):
#     print("Hey", name)
# greet()
# greet(name="satya")

# def show_scores(*scores):
#     print("Scores:",scores)
# def show_profile(**info):
#     print("Profile:", info)
# show_scores(80,90,35,45)
# show_profile(name="Satya", age=23)


# x=10
# def my_func():
#     x=5
#     print("Inside:", x)
# my_func()
# print("Outside:",x)

# x = 5
#
# def test():
#     # print(x)  # This will work
#     x = 10    # This line makes x LOCAL
#     print(x)
#
# test()

# tuple in python
# def func(*args):
#     print(args)
#
# func(1,2,2,45)


# def func(**kwargs):
#     print(kwargs)
# func(name="satya", age=21, occupation="student")


# def show_info(*args, **kwargs):
#     print("I got these numbers",args)
#     print("I got these labeled details", kwargs)
#
# show_info(1,2,3,22,1, name="Satya", country="India")


# def add_num(a, b):
#     res = a+b
#     return res
#
# sum_value = add_num(1, 70*2)
# print(sum_value)

# local variable
# def greet():
#     name="satya" #local variable
#     print(name)
# greet()

# global variable
# name="satya Prakash"
# def greet():
#     print ("Hello", name)
# greet()


# modifying a global variable
# count=0
# def increment():
#     global count
#     count+=1
#
# for i in range(1,10):
#     increment()
# print(count)


# import gc
# class Demo:
#     def __del__(self):
#         print("Object destroyed!")
# def create_object():
#     obj = Demo()
#     print("Object created inside function.")
# create_object()
# # Force Garbage Collector to run (optional)
# gc.collect()
# print("End of program.")

# What is Scope?
# Ans: Scope = Where a variable lives and dies. There are 2 main types: local and global

# "An object in Python lives as long as at least one variable refers to it. When references become 0, it is deleted automatically."
# import sys
#
# x = [1, 2, 3]
# print(sys.getrefcount(x))  # usually shows 2 (1 from x + 1 because passing it into getrefcount())

# my_list = [1, 2, 3, "hello", True]
# print(my_list)  # Output: [1, 2, 3, 'hello', True]
# print(my_list[3])  # Accessing an element by index


# my_tuple = (1, 2, 3, "hello", True)
# print(my_tuple)   # Output: (1, 2, 3, 'hello', True)
# print(my_tuple[1])  # Accessing an element by index


# my_set = {1, 2, 3, 3, 4, "hello"}
# print(my_set)  # Sets remove duplicates automatically.


# my_dict = {"name": "Satya", "age": 25, "language": "Python"}
# print(my_dict)
# print(my_dict["name"])  # Accessing the value by key


# add = lambda x,y: x+y
# print(add(5,6))

# num = [1,2,3,4,5]
# res = map(lambda x: x*x, num)
# print(list(res))