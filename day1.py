# print("Hello World!!")

# name="Satya"
# age=24
# height=6.2
# is_Student=False
#
# print(name,age, height, is_Student)
# print(type(height))


# personalized introduction
# # name = input("Enter your name: ")
# # age = input("enter your age: ")
# # print(f"Hello {name}! Your age is {age}.")
# print(type(int(age)))


# Sum, Product and Average
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the 2nd number: "))
# sum_result = num1 + num2
# product = num1*num2
# average = (num1+num2)/2;
# print(f"Sum of the nums are: {sum_result}")
# print(f"Product: {product}")
# print(f"And Average: {average}")
# ope = input("Your desired operator: ")
# if ope=="+":
#     print("You have choose {ope}")
#     print(num1+num2)
# elif ope=="-":
#     print("You have choosen {ope}")
#     print(num2-num1)
# elif ope=="*":
#     print("You have choosen {ope}")
#     print(num2 * num1)
# elif ope == '/':
#     if num2 == 0:
#         result = "Cannot divide by zero!"
#     else:
#         result = num1 / num2
# else:
#     result = "Invalid Operator"
# print(f"The result is:", result)

# age=int(input("Enter your age:"))
# citizen = True
# if age>=18 and citizen:
#     print("You are eligible to vote.")
# else:
#     print("You aren't elegible to vote.")

# val = bool(int(input("Enter 1 for True, 0 for False: ")))
# print(val)


# marks = int(input("Enter your marks:"))
# if marks>=90:
#     print("Grade: A")
# elif marks>=75:
#     print("Grade: B")
# elif marks>=60:
#     print("Grade: C")
# else:
#     print("Grade: D")



# Mini Project
# num = int(input("Enter any number:"))
# if num>0:
#     print("Positive number.")
# elif num<0:
#     print("Negative number")
# else:
#     print("Its a Zero!!")
# if num%2==0:
#     print("Its an Even number.")
# else:
#     print("Its an Odd Number")

# count=1
# while count<=5:
#     print("Count is:",count)
#     count+=1

# for i in range(5,0,-1):
    # print("i is :",i)

# for char in "Satya":
#     print(char)

# num=int(input("Enter a number: "))
# for i in range(1,num+1):
#     #even or odd
#     even_odd = "Even" if i%2==0 else "Odd"
#     #multiple of 3
#     mul_3 = "Multiple of 3" if i%3==0 else "Not a a multiple of 3"
#     #Square of the number
#     sqr = i ** 2
#     print(f"{i} is {even_odd} | {mul_3}| Square:{sqr}")


# total=0
# num = int(input("Enter a number (0 to stop): "))
# while num!=0:
#     total+=num
#     num = int(input("enter a number(0 to stop!!!)"))
# print(total)


import random

def choose_difficulty():
    print("Choose Your Difficulty level:")
    print("1.Easy(10 attempts)")
    print("2.medium(7 attempts)")
    print("3.Hard(5 attempts)")
    choice = int(input("Enter your choice (1 / 2 / 3): "))
    if choice==1:
        return 10
    elif choice==2:
        return 7
    elif choice==3:
        return 5
    else:
        print("Invalid choice! Defaulting to Medium (7 attempts).")
        return 7

sec_num = random.randint(1,100)
guess = None
attempts = 0
max_attempts = choose_difficulty()
print(f"Im thinking of a number between 1 and 100...")
print(f"You have {max_attempts} attempts. Good luck!!")
# loop until the guess is correct or attempts runs out
while guess != sec_num and attempts<max_attempts:
    guess = int(input("Take a guess: "))
    attempts+=1
    if guess<sec_num:
        print("Too low")
    elif guess>sec_num:
        print("tOO High")
    else:
        print(f"You have guessed the number in {attempts} tries!!")
        break
if guess != sec_num:
    print(f"Sorry! You have used all {max_attempts} attempts. The correct number was {sec_num}")
