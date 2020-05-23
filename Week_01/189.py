"""
189. 旋转数组
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k - int(k/len(nums))*len(nums)
        a = len(nums)-k
        nums[:k], nums[k:] = nums[a:], nums[:a]
        return nums