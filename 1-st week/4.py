"""
https://leetcode.com/problems/largest-number/
?envType=daily-question&envId=2024-09-18
"""

class Solution:
    def compare(i, j):
        a, b = str(i), str(j)
        return (a + b > b + a) - (a + b < b + a)

    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"
        sorted_nums = sorted(nums, key=functools.cmp_to_key(Solution.compare), reverse = True)
        ans = ""
        for i in range(0, len(sorted_nums)) :
            ans += str(sorted_nums[i])
        return ans