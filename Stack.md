# question

```
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if len(path) == 0:
            return None
        
        stack = []
        path = path.split("/")
        
        for c in path:
            if not c or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        res = "/" + "/".join(stack)
        
        return res
```

