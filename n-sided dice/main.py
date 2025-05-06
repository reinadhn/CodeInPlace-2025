import random

def main():
    dice = input("How many sides does your dice have? ")
    dice = int(dice)
    dice = random.randint(1,dice)
    print(f"Your roll is {dice}")

if __name__ == '__main__':
    main()