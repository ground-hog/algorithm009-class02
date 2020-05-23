"""
66. 加一
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_nums = ''.join(str(i) for i in digits)
        int_nums = int(str_nums)
        int_nums += 1
        str_nums = str(int_nums)
        str_nums = list(str_nums)
        str_nums = [int(x) for x in str_nums]
        return str_nums

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            a = len(digits) -1 -i
            if digits[a] != 9:
                digits[a] = digits[a] + 1
                break
            else:
                digits[a] = 0
                if a == 0:
                    digits.insert(0, 1)
        return digits