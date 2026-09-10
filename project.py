import random

computer = random.choice([-1, 0, 1])
yourstr = input("Enter your choice (s = Snake, w = Water, g = Gun): ")
yourdict = {
    "s": 1,
    "w": 0,
    "g": -1,
}
reversedict = {
    1: "Snake",
    0: "Water",
    -1: "Gun",
}
if yourstr not in yourdict:
    print("Invalid choice!")
else:
    you = yourdict[yourstr]
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")
    if computer == you:
        print("It's a draw!")
    elif (
        (you == 1 and computer == 0) or    # Snake drinks Water
        (you == 0 and computer == -1) or   # Water damages Gun
        (you == -1 and computer == 1)      # Gun kills Snake
    ):
        print("You won! :)")
    else:
        print("You lose! :(")