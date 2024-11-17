"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 9999999
        i = 0
        s = 0
        for j in range(0, len(nums)):
            s += nums[j]
            while s >= target:
                ans = min(ans, j - i + 1)
                s -= nums[i]
                i += 1
        if ans != 9999999:
            return ans
        else:
            return 0
