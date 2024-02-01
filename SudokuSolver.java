import java.util.Arrays;
public class SudokuSolver {

    int[][][] boards = {
        {
            {0, 2, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 6, 0, 0, 0, 0, 3},
            {0, 7, 4, 0, 8, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 3, 0, 0, 2},
            {0, 8, 0, 0, 4, 0, 0, 1, 0},
            {6, 0, 0, 5, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 1, 0, 7, 8, 0},
            {5, 0, 0, 0, 0, 9, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 0, 4, 0}
        },
        {
            {0, 0, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0, 3, 0, 8, 5},
            {0, 0, 1, 0, 2, 0, 0, 0, 0},
            {0, 0, 0, 5, 0, 7, 0, 0, 0},
            {0, 0, 4, 0, 0, 0, 1, 0, 0},
            {0, 9, 0, 0, 0, 0, 0, 0, 0},
            {5, 0, 0, 0, 0, 0, 0, 7, 3},
            {0, 0, 2, 0, 1, 0, 0, 0, 0},
            {0, 0, 0, 0, 4, 0, 0, 0, 9}
        },

        {
            {3, 0, 6, 5, 0, 8, 4, 0, 0},
            {5, 2, 0, 0, 0, 0, 0, 0, 0},
            {0, 8, 7, 0, 0, 0, 0, 3, 1},
            {0, 0, 3, 0, 1, 0, 0, 8, 0},
            {9, 0, 0, 8, 6, 3, 0, 0, 5},
            {0, 5, 0, 0, 9, 0, 6, 0, 0},
            {1, 3, 0, 0, 0, 0, 2, 5, 0},
            {0, 0, 0, 0, 0, 0, 0, 7, 4},
            {0, 0, 5, 2, 0, 6, 3, 0, 0}
        }
    };

    public void solveSudoku(int[][] board) {
        dfs(board,0);
    }
    private boolean dfs(int[][] board, int d) {
        if (d==81) return true; //found solution
        int i=d/9, j=d%9;
        if (board[i][j]!=0) return dfs(board,d+1);//prefill number skip
        
        boolean[] flag=new boolean[10];
        validate(board,i,j,flag);
        for (int k=1; k<=9; k++) {
            if (flag[k]) {
                board[i][j]=k;
                if (dfs(board,d+1)) return true;
            }
        }
        board[i][j]=0; //if can not solve, in the wrong path, change back to '.' and out
        return false;
    }
    private void validate(int[][] board, int i, int j, boolean[] flag) {
        Arrays.fill(flag,true);
        for (int k=0; k<9; k++) {
            if (board[i][k]!=0) flag[board[i][k]]=false;
            if (board[k][j]!=0) flag[board[k][j]]=false;
            int r=i/3*3+k/3;
            int c=j/3*3+k%3;
            if (board[r][c]!=0) flag[board[r][c]]=false;
        }
    }

    public void printBoards(int[][][] boards) {
        StringBuilder result = new StringBuilder();

        for (int n = 0; n < 3; n++) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    result.append(boards[n][i][j]).append(" ");
                }
                result.append("\n");
            }
            result.append("\n");
        }

        System.out.print(result.toString());
    }
    public void solveAll() {
        printBoards(boards);
        for (int[][] board : boards) {
            solveSudoku(board);
        }
        printBoards(boards);
    }

    public static void main(String[] args) {
        SudokuSolver s = new SudokuSolver();
        long start = System.currentTimeMillis();
        s.solveAll();
        long end = System.currentTimeMillis();

        System.out.println(end-start);
    }
}


