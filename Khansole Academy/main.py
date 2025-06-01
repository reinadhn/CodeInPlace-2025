import random

def main():
    print("Khansole Academy")
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    result = a + b

    print(f"What is {a} + {b}?")
    answer = int(input("Your answer: "))

    if answer == result:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {result}")

    
    
if __name__ == '__main__':
    main()