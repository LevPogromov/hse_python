"""
https://leetcode.com/problems/longest-nice-subarray/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        cur = nums[0]
        longest = 1
        i = 0
        for j in range(1, len(nums)):
            while i != j and nums[j] & cur != 0:
                cur -= nums[i]
                i += 1

            longest = max(longest, j - i + 1)
            cur += nums[j]
        return longest
