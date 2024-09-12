"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730411307"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

player_1: int = int(input("Pick a secret boat location between 1 and 4: "))
if player_1 < 1: 
    print("Error!", player_1, "too low!")
    exit()
  
if player_1 > 4: 
    print("Error!", player_1, "too high!")
    exit()

player_2: int = int(input("Guess a number between 1 and 4: "))
if player_2 < 1:
    print("Error!", player_2, "too low!")
    exit()

if player_2 > 4: 
    print("Error!", player_2, "too high!")  
    exit()

result: str = ""
if player_2 == (player_1):
    print("Correct!", "You hit the ship.")
    result = RED_BOX
else: 
    print("Incorrect!", "You missed the ship.")
    result = WHITE_BOX

 
if player_2 == 1:
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        
if player_2 == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)

if player_2 == 3:
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)

if player_2 == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
