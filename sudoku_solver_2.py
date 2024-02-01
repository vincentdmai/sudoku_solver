import numpy as np
import time

'''
3x3 Boards Problem Set
'''

boards = [
  [
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 3],
    [0, 7, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 2],
    [0, 8, 0, 0, 4, 0, 0, 1, 0],
    [6, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 7, 8, 0],
    [5, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
  ],

  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
  ],

  [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
  ]
]


def dfs(board, d):
  if d == 81:
    # DUB
    return True
  
  i = d // 9
  j = d % 9

  flags = np.full(10, True, dtype=bool)
  if board[i][j] != 0:
    return dfs(board, d+1)

  validate(board, i , j, flags)
  for k in range(1,10):
    if flags[k]:
      board[i][j] = k
      if dfs(board, d+1):
        return True
  board[i][j] = 0
  return False
  
def validate(board, i, j, flags):
  flags.fill(True)
  for k in range(9):
    if board[i][k] != 0:
      flags[board[i][k]] = False
    
    if board[k][j] != 0:
      flags[board[k][j]] = False

    r = i // 3 * 3
    c = j // 3 * 3

    if board[r][c] != 0:
      flags[board[r][c]] = False

start =time.time()
for board in boards:
  print(board)
  dfs(board, 0)
  print(board)
end = time.time()

print(end*1000 - start * 1000)
