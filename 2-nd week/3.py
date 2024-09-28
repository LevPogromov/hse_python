"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        cnt = 0
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if not stack:
                    cnt += 1
                else:
                    stack.pop()
        ans = cnt // 2
        if cnt % 2 != 0:
            ans += 1
        return ans
