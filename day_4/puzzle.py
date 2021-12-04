import numpy as np

# Calculates the sum of the unmarked board numbers.
def sum_unmarked(board, board_mask):
    return sum(sum(board * (1 - board_mask)))       # Perform elementwise multiplication between the two arrays.
                                                    # (1 - board_mask) flips the 1s and 0s to enable this multiplication.

def first_challenge():

    # List of all bingo boards in the input.
    all_boards = []

    # List of "masks" for all bingo boards where the drawn values are stored for each corresponding board.
    board_masks = []

    # Initialize various variables to avoid any errors.
    current_board = np.zeros((5, 5))
    winning_board = np.zeros((5, 5))
    winning_mask = np.zeros((5, 5))
    winning_num = -1
    i = 0

    # This for loop saves the bingo boards in memory and initializes the board masks.
    for line in lines:
        if line == '\n':
            current_board = np.zeros((5, 5))
            i = 0  # i serves as the row index of a board here
        else:
            current_board[i] = [int(x) for x in line.split()]
            i += 1

            # If i == 5, the board is finished and can be appended to the list.
            if i == 5:
                all_boards.append(current_board)
                board_masks.append(np.zeros((5, 5)))

    # Iterate over all drawn numbers and fill the board masks accordingly until a board has won.
    for num in drawn_numbers:
        for board, board_mask in zip(all_boards, board_masks):
            for i in range(board.shape[0]):  # Iterate over boards of the board
                for j in range(board.shape[1]):  # Iterate over columns of the board
                    if board[i][j] == num:
                        board_mask[i][j] = 1
                        break       # This could perhaps be improved by using for/else and breaking out of the outer loop (too).

            # Calculate the sums of all rows and columns of a board mask to see if the board wins.
            if board.shape[0] in board_mask.sum(axis=0) or board.shape[1] in board_mask.sum(axis=1):
                winning_board, winning_mask, winning_num = board, board_mask, num
                break

        # Check if winning_board is non zeros -> if a winning board has been found.
        if winning_board.any():
            unmarked_sum = sum_unmarked(winning_board, winning_mask)
            print(f'Sum of unmarked numbers: {unmarked_sum}')
            print(f'Winning drawn number: {winning_num}')
            print(f'unmarked_sum * winning_num: {unmarked_sum * winning_num}')
            break


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # Get numbers that will be drawn and detach them from the rest of the list.
    drawn_numbers = [int(x) for x in lines.pop(0).split(',')]

    first_challenge()

