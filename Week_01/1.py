"""
1. 两数之和
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_num = {}
        for i  in range(len(nums)):
            if target - nums[i] in dic_num:
                return [i, dic_num[target - nums[i]]]
            dic_num[nums[i]] = i