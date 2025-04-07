import random

choices = ("rock", "paper", "scissor")
Playing = True

while Playing:

    player = input("choose(rock,paper,scissor)")
    machine = random.choice(choices)
    
    
    if player == "quit":
        break

    if player !="rock" and player !="paper" and player !="scissor":
        player = input("choose(rock,paper,scissor)")
        
    print(f"player:{player}")
    print(f"machine:{machine}")

    if player == machine :
        print("Tie")
    elif player == "rock" and machine == "scissor" :
        print("Player won")
    elif player == "paper" and machine == "rock" :
        print("Player won")
    elif player == "paper" and machine == "rock" :
        print("Player won")
    else:
        print("machine won")

    