"""
https://leetcode.com/problems/max-consecutive-ones-iii/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i + 1
