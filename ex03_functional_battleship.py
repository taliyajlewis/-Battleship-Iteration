"""EX03 - Functional Battleship."""
 
__author__ = "730411307"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def input_guess(size_of_grid: int, id: str) -> int: 
    assert id == "row" or id == "column"

    result = -1
    while not (1 <= result <= size_of_grid):
        result = int(input(f"Guess a {id}: "))
        if not (1 <= result <= size_of_grid):
            print(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: ")
                         
    return result

def print_grid(size_of_grid: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    row_count = 1
    while row_count <= size_of_grid:
        row_string: str = ""
        column_count = 1

        while column_count <= size_of_grid:
            if row_count == row_guess and column_count == column_guess and correct_guess:
                row_string += RED_BOX
            elif not correct_guess and row_count == row_guess and column_count == column_guess:
                row_string += WHITE_BOX
            else:
                row_string += BLUE_BOX
            column_count += 1

        print(f"{row_string}")
        row_count += 1

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    return secret_row == row_guess and secret_column == column_guess

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    num_turn = 1
    total_turns = 5
    win = False

    while num_turn <= total_turns and not win:
        print(f"=== Turn {num_turn}/{total_turns} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        win = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, win)

        if win:
            print(f"Hit! You won in {num_turn}/5 turns!")
        else:
            print("Miss!")
        
        num_turn += 1
    
    if not win: 
        print(f"X/{total_turns} - Better luck next time!")