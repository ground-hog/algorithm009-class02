class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        res = []
        def backtrack(dic, path):
            if len(path) == len(nums):
                res.append(path)

            for i in dic.keys():
                if dic[i] == 0:
                    continue
                dic[i] -= 1
                backtrack(dic, path+[i])
                dic[i] += 1
        backtrack(dic,[])
        return res