import random
import re


def errorMessage():
    print(
        "Invalid Input ! Please guess the 4 colors 'BASED ON THE GIVEN COLOR CODE' and 'NOT GUESS LESS/MORE THAN "
        "4' "
        "COLORS (no space): ")


# Main Menu
def menu():
    print(" ___________________________ Welcome to the Mastermind Game _________________________")
    print("|There are 4 random given colors. Please guess the color using the given code below: |")
    print("|R = Red                                                                             |")
    print("|G = Green                                                                           |")
    print("|B = Blue                                                                            |")
    print("|Y = Yellow                                                                          |")
    print("|____________________________________________________________________________________|")


menu()

# Pre-Set the 4 Colors
colors = ["R", "G", "B", "Y"]

# Shuffle the 4 Colors
colors_code = random.sample(colors, 4)

game = True


def choice():
    finish_game = input("\nDo you want to play again (Y/N)?").upper()

    if finish_game == "N":
        print("Thanks for the game! Bye!")
        exit()
    elif finish_game == "Y":
        game = True
        print("So, let's play again!")


while game:

    # User Input
    user = input("Guess the 4 Colors (no space): ").upper()

    while len(user) < 4 or len(user) > 4 or not re.match("^[R,G,B,Y]*$", user):
        errorMessage()
        user = input().upper()

    # Convert User Input from "Str" to "List"
    userList = list(user)

    # User Input correct in 1 Attempt
    if userList == colors_code:
        print("Congrats ! You guessed the correct color in just 1 try.")
        choice()

    else:

        # Initialize "counter" variable to keep track of Number of Attempts
        counter = 0

        while userList != colors_code:

            # Initialize "count" variable to track of how many correct guessed color from User Input
            count = 0

            # Create a List to store the correct color from User Input
            correct = ['0', '0', '0', '0']

            # Create a For-Loop to loop 4 times, since we have only 4 colors
            for i in range(0, 4):

                # To check whether User Input order match with Colors order
                if userList[i] == colors_code[i]:
                    count = count + 1

                    userList[i] = "1"
                    correct[i] = userList[i]

                else:
                    continue

            # When part of the colors are guessed correctly
            if count < 4 and count != 0:

                # Increase Number of Attempts when part of the color is guessed incorrectly
                counter = counter + 1
                
                print('\n')
                print("Not all colors are correct, but you did get", count, "color(s) correct! (below 1 indicate correct placing)")

                # To print out the List
                for c in correct:
                    print(c, end=' ')  # End = ' ' is for system to print the Result in 1 Line instead of Next Line
                print('\n')
                user = input("Guess the 4 Colors again: ").upper()

                while len(user) < 4 or len(user) > 4 or not re.match("^[R,G,B,Y]*$", user):
                    errorMessage()
                    user = input().upper()

                userList = list(user)

                # When none of the colors are guessed correctly
            elif count == 0:
                print('\n')
                #print(*correct, sep='')
                print(*correct)
                print("None of the colors are guessed in the correct order")
                user = input("Guess the 4 Colors again: ").upper()

                while len(user) < 4 or len(user) > 4 or not re.match("^[R,G,B,Y]*$", user):
                    errorMessage()
                    user = input().upper()

                userList = list(user)

        # User Input correct in multiple attempts
        if userList == colors_code:
            counter = counter + 1
            print('\n')
            print("Congrats ! You guessed the correct colors in", counter, "tries")
            choice()
