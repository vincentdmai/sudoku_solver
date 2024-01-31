import numpy as np
import multiprocessing
from multiprocessing import freeze_support

def is_valid(board, i, j, num):
    # Check if 'num' is valid in the given position (i, j)
    return (
        np.all(board[i, :] != num) and
        np.all(board[:, j] != num) and
        np.all(board[i//3*3:i//3*3+3, j//3*3:j//3*3+3] != num)
    )

def solve_sudoku_partial(board, start, end, result_queue):
    for d in range(start, end):
        i, j = divmod(d, 9)
        if board[i, j] == 0:
            for num in range(9, 0, -1):
                if is_valid(board, i, j, num):
                    board[i, j] = num
                    if solve_sudoku(board):
                        result_queue.put(board.copy())
                    board[i, j] = 0

def solve_sudoku(board):
    empty_cells = np.argwhere(board == 0)  # Find indices of empty cells
    if len(empty_cells) == 0:
        return True  # The puzzle is already solved

    i, j = empty_cells[0]
    for num in range(9, 0, -1):
        if is_valid(board, i, j, num):
            board[i, j] = num
            if solve_sudoku(board):
                return True
            board[i, j] = 0  # Backtrack if the current configuration is invalid

    return False

def parallel_solve_sudoku(board):
    num_processes = multiprocessing.cpu_count()
    result_queue = multiprocessing.Queue()
    processes = []

    for i in range(num_processes):
        start = (i * 81) // num_processes
        end = ((i + 1) * 81) // num_processes
        process = multiprocessing.Process(target=solve_sudoku_partial, args=(board, start, end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not result_queue.empty():
        solution = result_queue.get()
        if np.all(solution):
            np.copyto(board, solution)
            return True

    return False

if __name__ == '__main__':
    freeze_support()

    # Example usage:
    sudoku_board = np.array([
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ], dtype=int)

    if parallel_solve_sudoku(sudoku_board):
        print("Sudoku Solved:")
        print(sudoku_board)
    else:
        print("No solution found.")
