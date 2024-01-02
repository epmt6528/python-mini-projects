import random


def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive number.")


top_of_range = get_valid_input("Type a number: ")
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = get_valid_input("Make a guess: ")

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses.")
