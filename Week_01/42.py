"""
42.接雨水
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[i]) - height[top]
                dist = i - stack[-1] - 1
                res += (dist * h)
            stack.append(i)
        return res