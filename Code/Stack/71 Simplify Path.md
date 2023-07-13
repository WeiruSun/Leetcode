# Simplify Path



Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.



## note
数据结构：stack

返回值： res (string)

解题： 遍历path

A. 如果当前值为“/”, 则忽略

B. 如果当前值为“..”,则删去
返回时对当前stack里进行join操作（加上“/）

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

