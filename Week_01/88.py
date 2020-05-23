"""
88. 合并两个有序数组
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
            return nums1
        if n == 0:
            return nums1
        p = m - 1
        q = n - 1
        for i in range(len(nums1)):
            a = len(nums1) -1 -i
            if nums1[p] <= nums2[q]:
                nums1[a] = nums2[q]
                if q == 0:
                    break
                q -= 1
            else:
                nums1[a] = nums1[p]
                if p == 0:
                    nums1[:a] = nums2[:a]
                    break
                p -= 1
        return nums1