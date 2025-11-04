class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def iscol(board, row, col, n):
            i = col
            while i >= 0:
                if board[row][i] == "Q":
                    return False
                i -= 1

            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True

        res = []

        def n_queen(board,col,n):
            
            if col == n:

                res.append(["".join(r) for r in board])
                return

            for row in range(n):

                if iscol(board,row,col,n):

                    board[row][col] = "Q"

                    n_queen(board,col+1,n)

                    board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        col = 0
        n_queen(board,col,n)
        
        

        return res