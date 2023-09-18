# https://leetcode.com/problems/valid-sudoku/

import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowcheck=collections.defaultdict(list)
        columncheck=collections.defaultdict(list)
        squarecheck=collections.defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    if( board[r][c] in rowcheck[r] or board[r][c] in columncheck[c] or board[r][c] in squarecheck[(r//3,c//3)] ):
                        return False
                    rowcheck[r].append(board[r][c])
                    columncheck[c].append(board[r][c])
                    squarecheck[(r//3,c//3)].append(board[r][c] )

        return True


solver=Solution()
print(solver.isValidSudoku(      
[["5","5",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]) )