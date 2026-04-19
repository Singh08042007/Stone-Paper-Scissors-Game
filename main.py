import random
def game():
    while True:
        print("------ Welcome to this Game ------")
        print("Choose between 1 or 2 or 3 or 4")
        print("\n1. Stone")
        print("2. Paper")
        print("3. Scissor")
        print("4. Exit")

        a = input("Enter your choice: ")
        choices = ["1", "2", "3"]

        if a == "4":
            print("Thank you for playing")
            break
        if a not in choices:
            print("Invalid Choice")
            continue

        chose = random.choice(choices)
        print(f"Computer have choses: {chose}")
        if a == chose:
            print("You won!")
        else:
            print("You lost!")

game()
