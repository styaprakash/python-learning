
import analyzer

def main():
    try:
        num = int(input("Enter a number to analyze:"))
        if analyzer.is_even(num):
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

        if analyzer.is_positive(num):
            print(f"{num} is positive")
        else:
            print(f"{num} is negative")

        if analyzer.is_prime(num):
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")

    except ValueError:
        print("Please enter a valid Integer")

if __name__ == "__main__":
    main()
