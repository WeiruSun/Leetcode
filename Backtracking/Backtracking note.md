# 回溯算法

## 回溯算法本质
决策树的遍历过程，考虑：
1. 路径：已做出的选择
2. 选择列表：也就是你当前可以做的选择
3. 结束条件

## 回溯算法与DFS 的区别

回溯法在求解过程中不保留完整的树结构，而DFS记录完整的搜索树

## code template

```Python
result = []
def backtrack(路径，选择列表)：
    if(满足结束条件)：
        result.append(路径)
        return
    for 选择 in 选择列表：
        做选择
        backtrack(路径，选择列表)
        撤销选择
```

## 例题
全排列问题
