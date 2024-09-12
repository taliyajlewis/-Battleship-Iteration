"""EX02 -  One Shot Battleship."""
 
__author__ = "730411307"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

size_of_grid: int = 4
a_secret_row: int = 3
a_secret_column: int = 2

row: int = int(input("Guess a row: "))
while row < 1 or row > size_of_grid:
    print(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: ")
    row = int(input("Guess a row: "))

column = int(input("Guess a column: "))
while column < 1 or column > size_of_grid:
    print(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: ")
    column = int(input("Guess a column: "))

result: str = ""

hit = False
if row == a_secret_row and column == a_secret_column:
    result = RED_BOX
    hit = True    
else:
    result = WHITE_BOX

row_count = 1
while row_count <= size_of_grid:
    row_string: str = ""
    column_count = 1

    while column_count <= size_of_grid:
        if row_count == a_secret_row and column_count == a_secret_column and hit:
            row_string += result
        elif not hit and row_count == row and column_count == column:
            row_string += WHITE_BOX
        else:
            row_string += BLUE_BOX
        column_count += 1

    print(f"{row_string}")
    row_count += 1

if hit: 
    print("Hit!") 
else:
    if row == a_secret_row:
        print("Close! Correct row, wrong column.")
    elif column == a_secret_column:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")