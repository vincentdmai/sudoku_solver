import numpy as np

'''
3x3 Boards Problem Set
'''

boards = [
  np.array([
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 3],
    [0, 7, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 2],
    [0, 8, 0, 0, 4, 0, 0, 1, 0],
    [6, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 7, 8, 0],
    [5, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
  ], dtype=int),

  np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
  ], dtype=int),

  np.array([
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
  ], dtype=int)
]

def solve_sudoku(board):
  """This solution modifies board in-place instead.

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

      Each of the digits 1-9 must occur exactly once in each row.
      Each of the digits 1-9 must occur exactly once in each column.
      Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

    The 0 value indicates empty cells.

    Args:
      board (list[list[int]]): List of list of ints representing the sudoku board
  """
  
  def is_valid(board, i, j, num):
    # Check if 'num' is valid in the given position (i, j)
    return (
      np.all(board[i, :] != num) and
      np.all(board[:, j] != num) and
      np.all(board[i//3*3:i//3*3+3, j//3*3:j//3*3+3] != num)
    )

  def solve(board):
    empty_cells = np.argwhere(board == 0)  # Find indices of empty cells
    for index in empty_cells:
      i, j = index
      for num in range(1,10):
        if is_valid(board, i, j, num):
          board[i, j] = num
          if solve_sudoku(board):
            return True
          board[i, j] = 0  # Backtrack if the current configuration is invalid
      return False

  solve(board)


solve_sudoku(boards[0])
print(boards[0])