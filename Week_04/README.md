学习笔记
1.深度优先搜索和广度优先搜索
搜索、遍历
每个节点访问且仅访问一次
对于节点的访问顺序不限：
深度优先：递归、手动维护一个栈 Depth-First-Search
广度优先：手动维护一个队列 Breadth-First-Search
优先级优先：启发式搜索（深度学习范畴，应用于推荐算法、高级搜索算法等）

dfs模版：
def dfs(node):
    if node in visited:
      return
    visited.add(node):
    dfs(node.left)
    dfs(node.right)

bfs模版：
def bfs(graph, start,end):
    queue = []
    queue.append([start])
    visitied.add(start)
    While queue:
       node = queue.pop()
       visited.add(node)
       process(node)
       nodes = gennerate_related_nodes(node)
       queue.push(nodes)

2.贪心算法
贪心算法：每一步都选取当前最优，希望导致结局是全局最优的算法，不能回退。
动态规划：当下最优判断+可以回退
贪心算法：高效性，所求结果接近最优解，可作为辅助算法或者直接解决一些要求结果不特别精确的问题。
贪心算法适用场景：问题可以分解为子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。

3.二分查找
前提：
A.目标函数单调性
B.存在上下界
C.能够通过索引访问

代码模版：
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1

4.牛顿迭代法
