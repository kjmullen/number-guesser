import random  # importing random module

number_to_guess = random.randint(1, 9)  # the number to guess is chosen randomly between 1 & 9

user_guess = int(input("Guess my number. 1 - 9: "))

guesses = 1

while guesses < 5:
    if user_guess > number_to_guess:
        print("Too high.")
    else:
        print("Too low.")

    print("You used : {} / 5 guesses.".format(guesses))
    guesses += 1
    if number_to_guess - user_guess == 1 or number_to_guess - user_guess == -1: # +/- 1 from number prints out a "super close" message.
        print("That last guess was super close.")
    user_guess = int(input("Guess my number. 1 - 10: "))

    if user_guess == number_to_guess:
        print("You guessed it! The number was {}".format(number_to_guess))
        break
    if guesses == 5:
        print("You used all your guesses")
        break



# user_guess < number_to_guess
# user_guess > number_to_guess
# user_guess == number_to_guess is game over. while loop?
# show number of guesses taken
# user is close if number_to_guess - user_guess <= 1

