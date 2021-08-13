import random

passwords = { "joe": "world123", "jane": "hello123" }

def game():
    value = input("Please enter your guess (between 1 and 10): ")
    print('Entered value is', value)
    if value == random.randrange(1, 10):
        print("You won!")
    else:
        print("Try again")

if __name__ == "__main__":
    game()
