#Minimum ASCII Delete Sum for Two Strings

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
 
## note
目的：给出不共有字符的ASCII sum
数据结构： dp(m*n)

如果 s1[i-1] == s2[j-1],dp[i][j] = dp[i-1][j-1] + s1[i-1]的ACSII值

如不相等，dp[i][j]为max(dp[i - 1][j], dp[i][j - 1]) ,即取s1 或 s2 当前字符中较大的那个

dp[m][n]储存着相同字符的ASCII值的和


```
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        
        dp = [[0 for i in range(n+1)]for j in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        res = - dp[m][n]*2
        for c in s1:
            res += ord(c)
        for c in s2:
            res += ord(c)
            
        return res
```

