import random


print("******************************************************************************")
print("*                                                                            *")
print("*                  Welcome to our Number guessing game                       *")
print("*                                                                            *")
print("******************************************************************************")


start = int(input("Enter starting number where to start : "))
end = int(input("Enter ending number where to end : "))


print(f"You have to guessed between {start} to {end} , Let's start the game ")


computer = random.randint(start, end)
chance = 7   # This will give the user 7 chance so that user can only avail 7 chances 
guess = 0    # This ensures user to start initially with 0 


while guess < chance:
    guess += 1
    guess_number = int(input('Enter your guess: '))

    if guess_number == computer:
        print(f"congragulation you have win the match,computer has guessed {computer},you have guessed it in {guess}")
        break
    elif guess >= chance and guess != computer:
        print(f"better luck! Next Time You have got {computer} points ")
    elif guess_number > computer:
        print(f"This is too high please enter a lower number")
    elif guess_number < computer:
        print(f"the number is too lower please enter a higher number")
    else:
        print("an error occured please try again letter ")