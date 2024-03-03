import random
print("Welcome to Game")
options = ("rock" , "paper" , "scissors")
running = True
while running:
    player =  None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice(rock , paper , scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    '''playAgain = input("If you wnat play again enter y\nif you are not enter any letter: ").lower()
    if not playAgain == "y":
        running = False'''
    if not input("Play agin? (y/n): ").lower() == "y":
        running = False
print("Thanks for playing")