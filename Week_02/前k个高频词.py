class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        a = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:k]
        res = [int(x[0]) for x in a]
        return res