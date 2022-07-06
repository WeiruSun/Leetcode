# Surrounded Regions

## Question description
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

### solution
```
from queue import Queue
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == "O":
                        board[i][j] = "L"
                        self.helper([i,j],board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "L":
                    board[i][j] = "O"
                    
        return board
                        
    
    def helper(self,start,board):
        q = Queue()
        q.put(start)
        
        while not q.empty():
            current = q.get()
            xList = [-1,1,0,0]
            yList = [0,0,-1,1]
            for j in range(4):
                currentX = current[0] + xList[j]
                currentY = current[1] + yList[j]
                if 0 <= currentX < len(board) and 0 <= currentY < len(board[0]) and board[currentX][currentY] == "O":
                        board[currentX][currentY] = "L"
                        q.put([currentX,currentY])


```