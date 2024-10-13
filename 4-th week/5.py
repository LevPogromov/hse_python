"""
https://leetcode.com/problems/first-missing-positive/description/
?envType=problem-list-v2&envId=array&difficulty=HARD
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()
        ans = 1
        for num in nums:
            if num == ans:
                ans += 1
            elif num > ans:
                return ans
        return ans
