# Minesweeper

## Question description
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.### solution
```Python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        neighbors = []
        count = 0
        currentRow = click[0]
        currentCol = click[1]
        # find the neighbor mines of startPoint (?)
        for i in range(-1,2):
            for j in range(-1,2):
                newRow = currentRow + i
                newCol = currentCol + j
                # 判断出界
                if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]):
                    if board[newRow][newCol] == "M":
                        count +=1
                    # deal with other case?
                    elif count == 0 and board[newRow][newCol] == "E":
                        neighbors.append([newRow,newCol])
        
        if count == 0:
            for item in neighbors:
                board[item[0]][item[1]] = "B"
                self.updateBoard(board,item)
        else:
            board[click[0]][click[1]] = str(count)
        
        return board

```
