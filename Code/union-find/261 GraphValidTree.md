# Graph Valid Tree

## description
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

解题关键： 图中是否有环
什么是环：一条只有第一个和最后一个顶点重复的非空路径
判断图中是否有环的方法：
1. 拓扑排序
2. DFS
3. unionfind

union find 解法：
对于无向图来说，在遍历边（u-v）时，如果结点 u 和结点 v 的“父亲”相同，那么结点 u 和结点 v 在同一个环中。
对于有向图来说，在遍历边（u->v）时，如果结点 u 的“父亲”是结点 v，那么结点 u 和结点 v 在同一个环中。

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

