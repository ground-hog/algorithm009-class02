class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {}
        for i in bills:
            dic[i] = dic.get(i,0) + 1
            if i == 10:
                if 5 not in dic.keys() or dic[5] < 1:
                    return False
                else:
                    dic[5] = dic.get(5,0) - 1
            if i == 20:
                if 5 not in dic.keys() or dic[5] < 1:
                    return False
                else:
                    if 10 in dic.keys() and dic[10] > 0:
                        dic[5] = dic.get(5,0) - 1
                        dic[10] = dic.get(10,0) - 1
                    elif dic[5] > 2:
                        dic[5] = dic.get(5,0) - 3
                    else:
                        return False
        return True