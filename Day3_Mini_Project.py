def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return  False
    for i in range(3, int(n**0.5)+1, 2):
        if n%1==0:
            return False
    return True

while True:
    user_input = input("Enter a number (or type 'exit' to quit) ")
    if user_input.lower()=="exit":
        print("Goodbye!")
        break
    try:
        number= float(user_input)
    except ValueError:
        print("Invalid Input! Pls enter a valid input")
        continue

    print("\n--- Analysis Report ---")
    # 1.sign
    if number>0:
        print("The number is a positive")
    elif number<0:
        print("The number is a negative")
    else:
        print("The number is Zero(0)!!")

    # 2. Even or odd
    if number.is_integer():
        if number%2==0:
            print("The number is even")
        else:
            print("the number is odd")
    else:
        print("Its not a whole number, so even/odd check doesn't apply.")

    # 3. Whole or Decimal
    if number.is_integer():
        print("Its a whole number.")
    else:
        print("It has a decimal part.")

    # 4. prime check
    if number.is_integer() and number>0:
        if is_prime(int(number)):
            print("Its a prime number.")
        else:
            print("Its not a prime numer.")

    print("-----------------------\n")