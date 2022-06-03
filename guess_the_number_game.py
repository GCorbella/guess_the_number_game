from random import *
infinity = True
while infinity == True:
    new_game = 1
    while new_game == 1:
        name = input("Please, enter your name: ")

        print(f"Hello {name}, you have 8 tries to guess the number.")
        tries = 8
        number = randint(0,101)

        while tries > 0 and new_game == 1:
            answer = int(input("Please, enter your number: "))
            if answer == number:
                print(f"Good Job, {number} is the correct number.")
                q_new_game = input(f"Do you want to play again, {name}? y/n ")
                if q_new_game == "y":
                    new_game = 0
                elif q_new_game == "n":
                    print(f"Thank you for playing with us, {name}.")
                    infinity = False
                    new_game = 0
                else:
                    print("Enter a correct command, please.")
            elif answer > number:
                print(f"Wrong, the number is lower than {answer}.")
                tries -= 1
            elif answer < number:
                print(f"Wrong, the number is bigger than {answer}.")
                tries -= 1
            else:
                print(f"Please, insert a valid number.")

        if tries == 0:
            print("You have used all your tries :(")
            q_new_game = input(f"Do you want to play again, {name}? y/n ")
            if q_new_game == "y":
                new_game = 0
            elif q_new_game == "n":
                print(f"Thank you for playing with us, {name}.")
                infinity = False
                new_game = 0
            else:
                print("Enter a correct command, please.")