# question
## description
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
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
                        self.bfs([i,j],board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "L":
                    board[i][j] = "O"
        return board
    
    def bfs(self, start,board):
        q = Queue()
        q.put(start)
        
        while not q.empty():
            current = q.get()
            print("current",current) #[3,1]
            currentX = current[0]
            currentY = current[1]
            xList = [-1,1,0,0]
            yList = [0,0,-1,1]
            for i in range(4):
                newX = currentX + xList[i] #[2,1]
                newY = currentY + yList[i]
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] == "O":
                    print("neighbor",[newX,newY])
                    board[newX][newY] = "L"
                    q.put([newX,newY])                                   
```

