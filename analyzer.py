def is_even(num):
    return num%2 == 0

def  is_positive(num):
    return num>0

def is_negative(num):
    return num<0

def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

# test code — only runs when this file is executed directly
if __name__ == "__main__":
    print("Testing the analyzer function...")
    print(is_even(4))
    print(is_positive(-2))
    print(is_negative(68))
    print(is_prime(7))














