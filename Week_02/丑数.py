
"""
面试题49. 丑数
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i1 = 0
        i2 = 0
        i3 = 0
        if n == 1:
            return n
        while(n>1):
            a = min(nums[i1]*2, nums[i2]*3, nums[i3]*5)
            if a == nums[i1]*2:
                i1 += 1
            if a == nums[i2]*3:
                i2 += 1
            if a == nums[i3]*5:
                i3 += 1
            nums.append(a)
            n -= 1
        return a