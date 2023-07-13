# Number of Connected Components in an Undirected Graph

## description
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

### solution
```
class Solution:
    parent = []
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = []
        for i in range(n):
            self.parent.append(i)
        

        for nodes in edges:
            x = nodes[0]
            y = nodes[1]
            self.union(x,y)

        res = 0
        for i in range (0,n):
            if(self.parent[i]==i):
                res += 1
        
        return res
        
    def find (self,x):
        while (self.parent[x] != x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        # print("before union",self.parent)
        self.parent[rootX] = rootY
        # print("X is ",rootX)
        # print("Y is ",rootY)
        # print("after union", self.parent)
        
            
```

