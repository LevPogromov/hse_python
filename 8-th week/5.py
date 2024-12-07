"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        ans = float("inf")
        j = 0
        curr = 0
        if target < 0:
            return -1

        for i in range(len(nums)):
            curr += nums[i]
            while curr > target and j <= i:
                curr -= nums[j]
                j += 1
            if curr == target:
                ans = min(ans, len(nums) - (i - j + 1))

        return ans if ans != float("inf") else -1
