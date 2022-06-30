# Satisfiability of Equality Equations

## description
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(26)
        
        for equation in equations:
            f1 = equation[0]
            op = equation[1]
            f2 = equation[3]
            if(op == '='):
                l1 = ord(f1) - ord("a")
                l2 = ord(f2) - ord("a")
                uf.union(l1,l2)
        
        for equation in equations:
            f1 = equation[0]
            op = equation[1]
            f2 = equation[3]
            if(op == '!'):
                l1 = ord(f1) - ord("a")
                l2 = ord(f2) - ord("a")
                if uf.find(l1) == uf.find(l2):
                    return False
        
        return True
    
        
        
```

