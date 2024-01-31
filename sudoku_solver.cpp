#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        // Initialize the trackers
        std::vector<std::unordered_set<int>> cols(9, std::unordered_set<int>());
        std::vector<std::unordered_set<int>> rows(9, std::unordered_set<int>());
        std::vector<std::unordered_set<int>> cells(9, std::unordered_set<int>());

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '0';
                    rows[i].insert(num);
                    cols[j].insert(num);

                    int box_id = i / 3 * 3 + j / 3;
                    cells[box_id].insert(num);
                }
            }
        }

        // Backtracking function
        bool solved = false;
        backTrack(board, rows, cols, cells, 0, 0, solved);
    }

private:
    void backTrack(std::vector<std::vector<char>>& board, std::vector<std::unordered_set<int>>& rows,
                   std::vector<std::unordered_set<int>>& cols, std::vector<std::unordered_set<int>>& cells,
                   int i, int j, bool& solved) {
        if (i == 9) {
            solved = true;
            return;
        }

        int new_i = i + (j + 1) / 9;
        int new_j = (j + 1) % 9;

        if (board[i][j] != '.') {
            backTrack(board, rows, cols, cells, new_i, new_j, solved);
        } else {
            for (int num = 1; num <= 9; ++num) {
                int box_id = i / 3 * 3 + j / 3;
                if (rows[i].count(num) == 0 && cols[j].count(num) == 0 && cells[box_id].count(num) == 0) {
                    rows[i].insert(num);
                    cols[j].insert(num);
                    cells[box_id].insert(num);
                    board[i][j] = static_cast<char>(num + '0');

                    backTrack(board, rows, cols, cells, new_i, new_j, solved);

                    if (!solved) {
                        rows[i].erase(num);
                        cols[j].erase(num);
                        cells[box_id].erase(num);
                        board[i][j] = '.';
                    }
                }
            }
        }
    }
};

int main() {
    // Example usage
    Solution solution;
    std::vector<std::vector<char>> sudokuBoard = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    solution.solveSudoku(sudokuBoard);

    // Print the solved Sudoku board
    for (const auto& row : sudokuBoard) {
        for (char cell : row) {
            std::cout << cell << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
