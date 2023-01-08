
## Slicing window - 本质
维护一个窗口，不断滑动更新答案

## Slicing window - 代码逻辑
```python
left,right = 0,1

while right < len(s):
    window.add(s.right)
    right += 1
    
    while (window need shrink):
        window.remove(s[left])
        left +=1
```
