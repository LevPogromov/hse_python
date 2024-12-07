"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] == 0:
                cnt += 1
            while cnt > 1:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            ans = max(ans, j - i)
        return ans
