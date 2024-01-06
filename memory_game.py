import random

def configure_board():
    #function to fill the board randomly
    digit = list(range(1, 9)) * 2
    random.shuffle(digit)
    table = [digit[n:n+4] for n in range(0, 16, 4)]
    return table

def output_board(table, uncover):
    #This function will show the output board
    for i in range(4):
        for j in range(4):
            if uncover[i][j]:
                print(table[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

def track_card_position():
    #This function will track the card's position
    while True:
        row_col = input("Enter the row (1 to 4) and col (1 to 4) position of the pair: ")
        row, col = map(int, row_col.split())
        if 1 <= row <= 4 and 1 <= col <= 4:
            return row - 1, col - 1
        else:
            print("Invalid position. Please enter again.")

def launch_game():
    # Function to launchs and play the game.
    table = configure_board()
    uncover = [[False]*4 for _ in range(4)]
    output_board(table, uncover)
    compare_pairs = 0
    while compare_pairs < 8:
        row1, col1 = track_card_position()
        if uncover[row1][col1]:
            print("Card at this position already faced up. Select position again.")
            continue
        uncover[row1][col1] = True
        output_board(table, uncover)
        
        row2, col2 = track_card_position()
        if uncover[row2][col2]:
            print("Card at this position already faced up. Select position again.")
            uncover[row1][col1] = False
            output_board(table, uncover)
            continue
        uncover[row2][col2] = True
        output_board(table, uncover)
        
        if table[row1][col1] == table[row2][col2]:
            print("Pair match")
            compare_pairs += 1
        else:
            print("Pair do not match. Select again!")
            uncover[row1][col1] = False
            uncover[row2][col2] = False
            output_board(table, uncover)

def main():
    #This function calls the launch game function to start and play the game. 
    launch_game()

main()