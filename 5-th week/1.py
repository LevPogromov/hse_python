"""
https://leetcode.com/problems/integer-to-roman/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        table = {}
        table[1] = "I"
        table[5] = "V"
        table[10] = "X"
        table[50] = "L"
        table[100] = "C"
        table[500] = "D"
        table[1000] = "M"
        table[4] = "IV"
        table[9] = "IX"
        table[40] = "XL"
        table[90] = "XC"
        table[400] = "CD"
        table[900] = "CM"
        ans = ""
        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while i <= num:
                ans += table[i]
                num -= i
        return ans
