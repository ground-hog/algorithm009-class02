class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(level,S):
            if level == 0:
                res.append(S)
                return
            if level > 0:
                for i in nums:
                    if i not in S:
                        recursion(level-1,S+[i])
        recursion(level = len(nums),S = [])
        return res