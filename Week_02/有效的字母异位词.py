class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = s.count(i)
        for j in t:
            if j not in dic2:
                dic2[j] = t.count(j)
        if dic1 == dic2:
            return True
        else:
            return False