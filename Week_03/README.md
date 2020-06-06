学习笔记
树的面试题解法一般都是递归，主要原因：1.节点的定义就是用递归的方式进行；2.树本身的重复性（自相似性）
递归：通过函数体来进行的循环
def recursion(level,param1,param2,...):
    #recursion terminator(递归终结条件)
    if level>MAX_LEVEL:
     process_result
     return

    #process logic in current level(处理当层逻辑）
     proces(level, data...)

    #drill down（下探到下一层）
     self.recursion(level+1,p1...)

    #reverse the current level status if nedded（清理当前层）
递归的思维要点：
1.不要人肉进行递归（最大误区）
2.找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3，数学归纳法的思维

分治、回溯是一种特殊的或者较为复杂的递归。
算法问题，找最近重复性（分治、回溯）或者最优重复性（动态规划）。
分治：将原问题分解为多个子问题


