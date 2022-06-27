# Graph Valid Tree

## description
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
```
class UnionFind:
    parents = []
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    
    def find(self,x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.parents[rootX] = rootY
        return True
    
    def getCount(self):
        res = 0
        for i in range(len(self.parents)):
            if (self.parents[i] == i):
                res += 1
        return res

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = UnionFind(n)
        
        for nodes in edges:
            x = nodes[0]
            y = nodes[1]
            c= parents.union(x,y)
            if not c:
                return False
        if parents.getCount()>1:
            return False
        return True
            
        
```

