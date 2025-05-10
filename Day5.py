# # lists
# fruits = ["bannna", "apple", "orange"]
# num=[1,2,3,4,5]
# mixed = [True, "yes", 42]
from traceback import print_tb

# movies = ["pk", "dhoom2", "chava", "Avengers", "Black  Panther"]
# print(movies)
# # replace the 2nd move with any other movie
# movies[1]="Interstellar"
# print(movies)
# # Remove the last movie.
# movies.pop();
# print(movies)
# # Insert a new movie at the beginning.
# movies.insert(0,"Tere Naam")
# print(movies)


# Tuples in Python
# t=(1,2,3)
# print(t[0])        # Access by index
# print(len(t))      # Get length
# print(t.count(2))  # Count occurrences of a value
# print(t.index(3))  # Find index of a value

# students = [
#     ("Alice", 21, 8.6, True),
#     ("Bob", 20, 6.9, False),
#     ("Carol", 22, 9.1, True)
# ]
# for student in students:
#     name, age, gpa, passed = student
#     if passed:
#         print(f"{name} passed with GPA {gpa}")
#
# t = (1, 2, 3)
# my_dict = {t: "A tuple as a key!"}
# print(my_dict[t])


# # List Comprehension
# # new_list = [expression for item in iterable]
# squares=[x**2 for x in range(10)]
# print(squares)
#
# # List Comprehensions with Conditions
# even_numbers=[x for x in range(10) if x%2==0]
# print(even_numbers)
#
# even_squares = [x**2 for x in range(20) if x%2==0]
# print(even_squares)
#
# divisible_by_2_and_3 = [x for x in range(10) if x % 2 == 0 and x % 3 == 0]
# print(divisible_by_2_and_3)

# Nested List Comprehensions
# new_list = [ [expression for item in inner_iterable] for item in outer_iterable ]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# flattened = [element for row in matrix for element in row]
# print(flattened)
#
# # Create a 3x3 Multiplication Table
# multiplication_table = [[(i+1) * (j+1) for j in range(3)] for i in range(3)]
# print(multiplication_table)

# # set
# my_set = {1,2,3}
# my_set2 = set([1,2,3])
# print(my_set)
# print(my_set2)
#
# # common set operations
# # adding
# my_set.add(4)
# print(my_set)
#
# # Removing elements:
# my_set.remove(4)
# print(my_set)
#
# # Discarding Elements (|):
# my_set.discard(5)
# print(my_set)
#
# # Set Union
# set1 = {1,2,3}
# set2 = {3,4,5}
# res = set1|set2
# print(res)
#
# # Set Intersection (&):
# res2=set1&set2
# print(res2)
#
# # Set Difference(-):Finding elements that are in the first set but not the second:
# res3 = set1-set2
# print(res3)
#
# # Set Symmetric Difference (^):Finding elements that are in either of the sets, but not in both:
# res4=set1^set2
# print(res4)
#
# # Subset and Superset:
# set_new1={1,2}
# set_new2={1,2,3,4}
# # Subset: A.issubset(B) checks if set A is a subset of set B.
# print(set_new1.issubset(set_new2))
# # Superset: A.issuperset(B) checks if set A is a superset of set B.
# print(set_new2.issuperset(set_new1))


# # Dictionary: Basic a DS to store elements in a key-value pair. We can consider it as hashmap like in java
# student = {
#     "name": "Alice",
#     "age": 21,
#     "grades": [85, 69, 92]
# }
#
# # Accessing values
# # print(student["name"]) #one way to get the value of a key
# # print(student.get("age"))
# # print(student.get("gender", "Not specified")) #Default value
# # print(student.get("name")) #another way to get the value of a key
# # print(student.get("age"))
# # print(student.get("grades"))
#
# # Adding or updating
# student["major"]="cs"
# student["age"]=22
#
# # Deleting a key
# del student["grades"]
# print(student.get("grades"))
#
# #Iterating
# for key, value in student.items():
#     print(f"{key} -> {value}") # .items() => Returns (key, value) pairs
#
# # Key rules and edge cases
# # - keys must be immutable but values can be of any type.
# # - keys must be unique
# # - If you use a mutable object like a list as a key: ❌ Error (TypeError: unhashable type).
#
# # Nested dictionary
# database = {
#     "user1": {"name":"Alice", "age": 25},
#     "user2": {"name": "Satya", "age": 23}
# }
# print(database["user1"]["age"])
#
# students = {
#     "101": {
#         "name": "Alia",
#         "age": 20,
#         "grades": [90,25,36]
#     },
#     "102": {
#         "name": "SATYA",
#         "age":22,
#         "grades": [70,69,54]
#     }
# }
#
# # Accessing Nested Data
# print(students["101"]["name"])
# print(students["102"]["name"])
# print(students["102"]["grades"][1])
#
# # Adding Data to Nested Dict
# students["103"] = {
#     "name": "Charlie",
#     "age": 21,
#     "grades": [88,14,72]
# }
#
# # updating values
# students["101"]["age"] = 21 # one way to update the value
# students["102"]["grades"].append(16) # another way to update the value
#
# # Iterating over Nested Dist
# for student_id, info in students.items():
#     print(f"\nID: {student_id}")
#     for key, value in info.items():
#         print(f"{key}: {value}")
#
# students1 = {
#     "201": {"name": "John", "age": 22, "grades": [85, 90]},
#     "202": {"name": "Emma", "age": 23, "grades": [88, 76]},
#     "203": {"name": "Liam", "age": 21, "grades": [92, 81]}
# }
# for stud_id, ids in students1.items():
#     print(f"\n Student Id: {stud_id}")
#     for key, value in ids.items():
#         print(f"\t{key} : {value}")
#
# # code that prints only students whose average grade is greater than 85
# for student_id, info in students.items():
#     grades = info["grades"]
#     average = sum(grades) / len(grades)
#
#     if average > 85:
#         print(f"\nStudent ID: {student_id} (Average: {average:.2f})")
#         for key, value in info.items():
#             print(f"  {key}: {value}")

# String Manipulation

# s="Python"
# print(s[0])
# print(s[-1]) #backwards
# print(s[1:4]) # slicing
#
# # Common String Methods
# text = "  Hello, Python World!  "
#
# print(text.lower()) # convert to lower case
# print(text.upper()) # convert to upper case
# print(text.strip()) # Removes leading/trailing whitespace
# print(text.replace("Python", "Java")) #  Replace characters or substrings
# print(text.strip().split()) # Split into a list
# print("a-b-c".split("-"))
# words = ["Hello", "Python", "World"]
# print(" ".join(words)) # Join a list into string
# print("-".join(words))
# print(text.find("Python"))
# print(text.find("Java"))
# print(text.strip().startswith("Hello")) # Checks prefix
# print(text.strip().endswith("World!"))  # Checks suffix
# print(text.count("o")) # Count number of occurrences

# s1 = "   Learn Python Programming   "
# print(s1.strip())
# print(s1.lower())
# print(s1.upper())
# print(s1.strip().split())
# print("-".join(s1.strip()))
# print(s1.strip().startswith("Learn"))
# print(s1.strip().endswith("ing"))
# print(s1.count("P"))
# print(s1.find("Learn"))

# s = "MasterPython"
# print(s[0:6]) # Master
# print(s[6:12]) # Python
# # -ve indexing: Negative indexes count from the end
# print(s[-6:])  # Python
# print(s[:-3])   # MasterPyt
#
# print(s[::3])
# print(s[::-1]) #reverse the string in best way
# print(s[::-2])
#
# String Formatting in Python
name = "Alice"
age = 25
# Old - style formatting
print("My name is %s and im %d years old." % (name, age))
# str.format() method
print("My name is {} and im {} years old.".format(name,age))
# f-strings (Python 3.6+) ✅ Recommended
print(f"My name is {name} and im {age} years old.")

#
# # Check for pallindrome
# def is_palindrome(s):
#     s= s.strip().lower() # convert it to a stripped string in lower letters
#     return s==s[::-1] #reverse the string and compare
# print("is this a pallindrome string: ",is_palindrome("Racecar"))
# print("is this a pallindrome string: ",is_palindrome("Satya"))
#
# # Count Vowels and Consonants
# def count_VandC(s):
#     vowels = "aeiouAEIOU"
#     v=0
#     c=0
#     for charS  in s:
#         if charS.isalpha():
#             if charS in vowels:
#                 v+=1
#             else:
#                 c+=1
#     return v, c
# print(count_VandC("Learn Python"))
#
# # Anagram Checker
# def anagram_checker(s1, s2):
#     return sorted(s1.replace(" ","").lower()) == sorted(s2.replace(" ","").lower())
# print(anagram_checker("Listen", "Silent"))    # True
# print(anagram_checker("Hello", "World"))
#
# # Longest word in a sentence
# def longest_word(sentence):
#     words = sentence.split() # its convert an entire string to a char array
#     return max(words, key=len)
# print(longest_word("Python is fun and educational"))
#
# def long_word(sentence):
#     words = sentence.split()
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest
# print(long_word("Python is fun and Educational!"))