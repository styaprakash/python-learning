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