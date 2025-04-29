from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    fix_column()
    while front_is_clear():
        next_column()
        fix_column()

    
def fix_column():
    #This function is for Karel to put the beeper and go up until the front is blocked and back to where they start (using the original_column function)
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    if front_is_blocked():
        put_beeper()
    original_column()

def original_column():
    #This function is use for Karel to go back where they are start 
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def next_column():
    #This function is for move to the next column
    for i in range(4):
        move()

"""def not_duplicate():
    if put_beeper():
        pass
    else:
        put_beeper()"""

if __name__ == '__main__':
    main()