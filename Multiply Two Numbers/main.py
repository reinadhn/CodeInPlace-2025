"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    first_num = int(first_num)
    second_num = int(second_num)
    call = first_num*second_num
    print(call)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()