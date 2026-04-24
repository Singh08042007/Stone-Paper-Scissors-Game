import random
import utils

def game():
    while True:
        print("\n------ Welcome to this Game ------")
        print("1. Stone")
        print("2. Paper")
        print("3. Scissor")
        print("4. Show Score")
        print("5. Exit")

        a = input("Enter your choice: ")
        choices = ["1", "2", "3"]

        # Show Score
        if a == "4":
            win, loss = utils.get_score()
            print("\nCurrent Score:")
            print("Wins:", win)
            print("Losses:", loss)
            continue

        # Exit
        if a == "5":
            print("Thank you for playing!")
            break

        if a not in choices:
            print("Invalid Choice")
            continue

        chose = random.choice(choices)
        print(f"Computer chose: {chose}")

        # Game logic
        if a == chose:
            print("It's a draw!")
        elif (a == "1" and chose == "3") or \
             (a == "2" and chose == "1") or \
             (a == "3" and chose == "2"):
            print("You won!")
            utils.update_win()
        else:
            print("You lost!")
            utils.update_loss()

game()