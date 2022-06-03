from random import *
new_game = 1
while new_game == 1:
    name = input("Please, enter your name: ")

    print(f"Hello {name}, you have 8 tries to guess the number")
    tries = 8
    number = randint(0,101)

    while tries > 0:
        answer = int(input("Please, enter your number: "))
        if answer == number:
            print(f"Good Job, {number} is the correct number.")
            q_new_game = input("Do you want to play again? y/n ")
            while q_new_game != "y" or "n":
                if q_new_game == "y":
                    new_game = 0
                elif q_new_game == "n":
                    print("Thank you for playing with us.")
                    break
                else:
                    continue

        elif answer > number:
            print(f"Wrong, the number is lower than {answer}.")
            tries -= 1
        elif answer < number:
            print(f"Wrong, the number is bigger than {answer}.")
            tries -= 1
        else:
            print(f"Please, insert a valid number.")
            continue
    if tries == 0:
        print("You have used all your tries :(")
        q_new_game = input("Do you want to play again? y/n ")
        while q_new_game != "y" or "n":
            if q_new_game == "y":
                new_game = 0
            elif q_new_game == "n":
                print("Thank you for playing with us.")
                break
            else:
                continue