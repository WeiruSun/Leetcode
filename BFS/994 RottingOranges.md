# Rotting Oranges

## Question description
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

### solution
```
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if grid is None:
            return None
        
        fresh = 0
        q = Queue()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotPoint = [i,j]
                    q.put(rotPoint)
                if grid[i][j] ==1:
                    fresh +=1
        
        if fresh == 0:
            return 0
        
        counter = -1
        
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                rotOrange = q.get()
                neighbors = self.findNeighbor(grid,rotOrange)
                for neighbor in neighbors:
                    current = grid[neighbor[0]][neighbor[1]]
                    if current == 1:
                        grid[neighbor[0]][neighbor[1]] = 2
                        q.put(neighbor)
                        fresh -=1
            counter +=1
        
        if fresh == 0:
            return counter
        else:
            return -1
                    
            
    
    def findNeighbor(self,grid,rotOrange):
        neighborList = []
        rowNum = len(grid)
        colNum = len(grid[0])
        
        deltaX = [0,0,-1,1]
        deltaY = [1,-1,0,0]
        
        for i in range(4):
            x = deltaX[i]+ rotOrange[0]
            y = deltaY[i]+ rotOrange[1]
            if x >= 0 and x< rowNum and y >= 0 and y < colNum:
                neighborList.append([x,y])
        return neighborList
               
   

```