#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board (same dict), keeping main unchanged."""
    ROWS = ROW
    COLS = COL

    # Finding empty cell
    empty = False
    for r in ROWS:
        for c in COLS:
            if board[r + c] == 0:
                row = r
                col = c
                empty = True  
                break
        if empty:
            break

    # no empty cells
    if not empty:
        return board

    for num in range(1, 10):
        # Check row
        row_conflict = False
        for c in COLS:
            if board[row + c] == num:
                row_conflict = True
                break
        if row_conflict:
            continue

        # Check column
        col_conflict = False
        for r in ROWS:
            if board[r + col] == num:
                col_conflict = True
                break
        if col_conflict:
            continue

        # Check 3x3 box
        box_conflict = False
        box_row = (ROWS.index(row) // 3) * 3
        box_col = (COLS.index(col) // 3) * 3
        for row_i in range(3):
            for col_i in range(3):
                rr = ROWS[box_row + row_i]
                cc = COLS[box_col + col_i]
                if board[rr + cc] == num:
                    box_conflict = True
                    break
            if box_conflict:
                break
        if box_conflict:
            continue

        board[row + col] = num
        result = backtracking(board)

        # checking if solved
        solved = True
        for rr in ROWS:
            for cc in COLS:
                if result[rr + cc] == 0:
                    solved = False
                    break
            if not solved:
                break

        if solved:
            return result  

        board[row + col] = 0

    return board


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv[1]) < 9:
            print("Input string too short")
            exit()

        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')
    else:
        print("Usage: python3 sudoku.py <input string>")
    
    print("Finishing all boards in file.")
