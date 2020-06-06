class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def com(level,ls,start):
            if level == 0:
                res.append(ls)
            for i in range(start,n+1):
                com(level-1,ls+[i],i+1)
            return res
        res = com(level = k, ls = [],start =1)
        return res