"""
https://leetcode.com/problems/basic-calculator/description/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        num = 0
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            if c == "+":
                result += num * sign
                sign = 1
                num = 0
            if c == "-":
                result += num * sign
                sign = -1
                num = 0
            if c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            if c == ")":
                result += sign * num
                result *= stack[-1]
                stack.pop()
                result += stack[-1]
                stack.pop()
                num = 0
        result += num * sign
        return result
