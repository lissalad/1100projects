

# input = input("Greetings, what is your name? > ")
# print("Greetings", input)

# player = input("Bear, Ninja, or Cowboy? > ")
# print(player)

# import library for random
from random import randint

# make array
roles = ["Bear", "Ninja", "Cowboy"]

# generate random number
computer = roles[randint(0,2)]

player = False
score = 0
total = 0;

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role

    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
        score+=1
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
        score+=1
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)
        score+=1

    total+=1
    print(f"Score: {score}/{total}." )
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break


    


