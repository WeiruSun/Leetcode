# Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

## solution 1 : brute force
check every single substring, and we have n**2 substring

for every substring, we have to do a linear scan

so time complexity would be : O(n**3)

## solution 2: divide from center
find the left of the current string. check if palindromic or not. 

the time complexity would be n*n

but corner case is the palindrome is even

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    resLen = r-l +1
                    res = s[l:r+1]
                l -=1
                r +=1
            #even length
            l,r =i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    resLen = r-l +1
                    res = s[l:r+1]
                l -=1
                r +=1
        
        return res
```



## solution 3: dp with memorization
 ```Python
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

