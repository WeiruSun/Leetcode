# Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


## note:
数据结构：
* hash表
* res = []
* 指针：
left = 0
right = 0
* count = len(p)

将string p 中字母及其频率储存在hash表中
遍历string s(使用right指针)：
    对于当前字母

如果目前字母在哈希表里且频率为负， count - 1

如果count = 0 则加入left到res中

如果

```
```

