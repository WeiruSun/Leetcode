# question

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

question: 

- would s1 have repeat character? 

```
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        
        #create hashmap for two string
        s1Count,s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord("a")] +=1
            s2Count[ord(s2[i])-ord("a")] +=1
        
        match = 0

        for i in range(26):
            match += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        #already intitalize the window, start as len(s1)
        for r in range(len(s1),len(s2)):
            if match == 26:
                return True
            index = ord(s2[r])- ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                match +=1
            elif s1Count[index] + 1 == s2Count[index]:
                match -=1
            
            index = ord(s2[l])- ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                match +=1
            elif s1Count[index] - 1 == s2Count[index]:
                match -=1
            l += 1
        return match == 26
            
            
```

