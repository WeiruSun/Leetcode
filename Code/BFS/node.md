# BFS

## BFS vs DFS
1. BFS 与 DFS 本质上都是图的遍历: 
   - DFS 穷举路径      
   - BFS 穷举node的状态
2. BFS 找到的路径最短，但空间复杂度比DFS 大

## BFS 写法
使用队列，每次将一个节点周围的所有节点加入队列

## BFS 问法
在“图”中找到起点到终点的最近距离
其中变体有：
1. 走迷宫
2. 替换单词
3. 连连看

## BFS 框架
```python
def BFS(self,start,target):
   q = Queue() #数据结构：queue
   visited = set() #数据结构set:避免走回头路
   
   q.put(start)#将起点加入queue
   visited.add(start)
   
   step = 0 #记录扩散的步数
   
   while not q.empty():
      qSize = q.size() #当前层级有多少node
      #将队列中所有节点向四周扩散
      for i in range(qSize):
         current = q.pop()
         #判断是否到达终点
         if current == target:
            return step
         #将current周围的node放进队列
         for node in current.adj():
            if node not in visited:
               q.put(node)
               visited.add((node))
    step += 1
   
            
         
         
   

```




 

 




