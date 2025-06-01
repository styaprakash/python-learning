# class Dog:
#     def __init__(self, breed):
#         self.breed = breed
#
# #creating object
# d1 = Dog("Labrador")
# print(d1.breed)
# from cgi import print_form
# from doctest import Example
from wadllib.application import ResourceType


# # Instance vs Class Variables
# class Dog:
#     species = "canine" # class variable
#
#     def __init__(self,breed):
#         self.breed = breed # instance variable (unique per object)
# dog1 = Dog("Labrador")
# dog2 = Dog("Husky")
# print(dog1.species, dog2.breed)

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def speak(self):
#         return f"{self.name} is barking!"
#
# # Creating objects
# dog1 = Dog("billie","husky")
# dog2 = Dog("alice", "pug")
#
# # calling methods
# print(dog1.speak())
# print(dog1.breed)
# print(dog2.speak())
# print(dog2.name)


# Inheritance


# # Single Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} makes a sound."
#
# class Dog(Animal): #Dog inherits from Animal
#     def speak(self):
#         return f"{self.name} says woof!"
# a = Animal("Generic Animal")
# b = Dog("Buddy")
# print(a.speak())
# print(b.speak())

# Multiple inheritance:In multiple inheritance, a class inherits from more than one parent class.
# Python allows this, but we must be careful to avoid method conflicts.
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
#
# class Canine:
#     def type_of_animal(self):
#         print("Canine family")
#
# class Dog(Animal, Canine):
#     def speak(self):
#         print("Dog Barks")
#
# dog = Dog()
# dog.speak()
# dog.type_of_animal()
# print(Dog.__mro__) # Method Resolution Order (MRO)

# # Example 2
# class Father:
#     def skills (self):
#         print("Gardening, Carpentry")
# class Mother:
#     def skills(self):
#         print("Cooking, Painting")
# class Child(Father, Mother):
#     # def skills(self):
#     #     print("Cooking1, Painting1")
#     pass
#
# c = Child()
# c.skills()
# print(Child.__mro__)


# # Custom Example with super()
# class A:
#     def show(self):
#         print("A's show method")
# class B:
#     def show(self):
#         print("B' shows method")
#
# class C(A, B):
#     def show(self):
#         super().show() #calls the method from the first parent class in MRO
#
# c=C()
# c.show()
#
# # Using All Parent Methods
# class A:
#     def show(self):
#         print("A's show")
# class B:
#     def show(self):
#         print("B's show")
#
# class C:
#     def show(self):
#         A.show(self)
#         B.show(self)
#
# c = C()
# c.show()
#
# # Potential Problem: Diamond Problem
# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
#
# class D(B,C):
#     pass
#
# print(D.__mro__)
# d=D()
# d.show()

# # What is Multilevel Inheritance? :In multilevel inheritance, a class inherits from a class which itself inherited from another class.
# class Animal:
#     def speaks(self):
#         print('Animal Speaks.')
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks Wooof!")
# class Puppy(Dog):
#     def weep(self):
#         print("Puppy weeps.")
# p=Puppy()
# p.speaks()
# p.bark()
# p.weep()
#
# # Real-World Example: Banking System
# class BankUser:
#     def login(self):
#         print("User logged in")
#
# class Customer(BankUser):
#     def view_account(self):
#         print("Viewing account balance")
#
# class PremiumCustomer(Customer):
#     def request_loan(self):
#         print("Loan request submitted")
#
# # Create object of PremiumCustomer
# user = PremiumCustomer()
# user.login()          # From BankUser
# user.view_account()   # From Customer
# user.request_loan()   # From PremiumCustomer



# # What is Hierarchical Inheritance? In Hierarchical Inheritance, multiple subclasses inherit from a single parent class.
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def introduce(self):
#         print(f"My name is {self.name}")
#
# class Student(Person):
#     def study(self):
#         print(f"{self.name} is studying.")
# class Teacher(Person):
#     def teach(self):
#         print(f"{self.name} is teaching.")
#
# student = Student("Alice")
# teacher = Teacher("Amanda")
#
# student.introduce() # this comes from Person class
# student.study() #this comes from Student class
#
# teacher.introduce()
# teacher.teach()



# Hybrid Inheritance is a combination of two or more types of inheritance (like multiple + multilevel + hierarchical) used together.
# It can lead to complex class hierarchies, and Python uses the Method Resolution Order (MRO) to handle it.
class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def who_am_i(self):
#         return f"I am a person named {self.name}"
#
# class Student(Person):
#     def __init__(self, name, student_id):
#         Person.__init__(self,name)
#         self.student_id = student_id
#
#     def get_role(self):
#         return f"{self.name} is a student with ID {self.student_id}"
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         Person.__init__(self,name)
#         self.subject = subject
#
#     def get_role(self):
#         return f"{self.name} teaches {self.subject}"
#
# class TeachingAssistant(Student, Teacher):  # Hybrid Inheritance
#     def __init__(self, name, student_id, subject):
#         Student.__init__(self, name, student_id)
#         Teacher.__init__(self, name, subject)
#
#     def get_role(self):
#         return f"{self.name} is a TA (Student ID: {self.student_id}) and teaches {self.subject}"
#
# # Test
# ta = TeachingAssistant("Alice", "S123", "Python")
# print(ta.who_am_i())        # From Person
# print(ta.get_role())        # Overridden in TeachingAssistant
# print(TeachingAssistant.__mro__)  # See method resolution order
#