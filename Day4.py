# # Positional arguments
# def greet(name, city):
#     print(f"Hello {name} from {city}!")
# greet("Alice", "Berlin")
#
# # Keyword Arguments
# greet(city="Delhi", name="Satya")

# # Default Arguments
# def greet(name, city="Bbsr"):
#     print(f"Hello {name} from {city}!")
# greet("Charlie")
# greet("Charlie", "Goa")

# # *args Collects extra positional arguments into a tuple
# def add(*num):
#     print(num)
#     print(sum(num))
# add(1,2,3,4)

# # **kwargs → Collects extra keyword arguments into a dictionary
# def profile(**details):
#     print(details)
# profile(name="Jhon", age=30, country="India", marks=69.91, )

# def smart_calculator(a,b,*args, operation="add", **kwargs):
#     result = None
#     numbers = (a,b) + args
#     if operation==  "add":
#         result = sum(numbers)
#     elif operation == "mul":
#         result=1
#         for num in numbers:
#             result *= num
#     else:
#         print("Unsupported Option!!")
#         return
#     if kwargs.get("round_result"):
#         result=round(result)
#     return result
#
# print(smart_calculator(1.5, 2.5, round_result=True))
# print(smart_calculator(2,3,4,5,operation="mul"))
# print(smart_calculator(2,2,2,2,2,operation="add", round_result=True))

# import utils

# utils.greet("Alice")

# Function Arguments & Variable Scope Recap
# x="global"
# def outer():
#     x="enclosing"
#     def inner():
#         x="local"
#         print("Inside inner:", x)
#     inner()
#     print("Inside Outer:", x)
# outer()
# print("Outside:", x)

# x=5
# def change_x():
#     x=10
#     print("Inside function:", x)
# change_x();
# print("Outside function:", x)


# def change_x():
#     global x
#     x=10
#     print("Inside function:", x)
# change_x();
# print("Outside function:", x)


# # Lambda Function revisited
# add = lambda x,y: x+y
# print(add(25,23))

# # map() with lambda
# nums=[1,2,3,4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

# # filter() with lambda
# nums = [1,2,3,4]
# even = list(filter(lambda x: x%2, nums))
# print(even)

# # sorted() with lambda(custom sort)
# pairs = [(1,3),(2,2),(4,1)]
# sorted_pairs = sorted(pairs, key=lambda x: x[1])
# print(sorted_pairs)

# def square(num):
#     print(num ** 2)
#
# result = square(4)  # Output: 16
# print(result)       # Output: None

def square(num):
    return num ** 2

result = square(4)
print(result)   # 16
