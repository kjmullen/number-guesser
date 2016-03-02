# HARD MODE
# user gives number  user_number = int(input("Pick a number. I'm going to try to guess it."))
# computer picks number in range

import random

user_number = int(input("Pick a number 1-9. I'm going to try to guess it... "))


def number_guesser():
    """
    Computer gets 5 guesses to guess a number 1-9
    User responds with y, n, or already guessed that
    """
    computer_guesses = 0
    while computer_guesses < 5:
        computer_guess = random.randint(1,9)
        print("Is your number {}? ".format(computer_guess))
        computer_guesses += 1
        user_response = input("Y / N / ALREADY GUESSED THAT? ").lower()
        if user_response == "y":
            print("Gotcha!")
            if user_number != computer_guess:
                print("Really? You forgot your number was {}.".format(user_number))
            break
        elif user_response == "n":
            continue
        elif user_response in "already guessed that":
            computer_guesses -= 1
            print("Whoops.")
            continue
        if computer_guess not in user_number:
            print("Whoops.")
        return computer_guess


number_guesser()


# buggy code / couldn't get the message of overall failure to display after 5 guesses
# while computer_guess != user_number and computer_guesses == 5:
#     print("Failed.")
# trying to do a message if computer failed to guess.
# while computer_guesses == 5:
#    if computer_guess != user_number:
#        print("Failed.")


# # # Problems # # #
# computer guesses same number too many times
# need a list of already guessed numbers that computer will stop using
#  - make empty list, append already guessed numbers to it, run while loop
#  - that'll continue doing the code without repeating numbers
# code requires a lot more user interaction (having to tell the computer it already guessed that number)
# accuracy depends more on user

