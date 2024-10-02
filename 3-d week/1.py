"""
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
?envType=daily-question&envId=2024-10-01
"""


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = [0 for i in range(0, k)]
        for num in arr:
            remainder[(num % k + k) % k] += 1
        if remainder[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if remainder[i] != remainder[k - i]:
                return False
        return True
