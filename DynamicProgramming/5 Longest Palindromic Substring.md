# Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
 ```
 class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0 or n == 1:
            return s
        
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(res) < len(s[i:j+1]):
                            res = s[i:j+1]
        return res
                
        
```

