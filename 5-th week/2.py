"""
https://leetcode.com/problems/random-pick-index/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        flag = 0
        while flag == 0:
            ind = randint(0, len(self.nums) - 1)
            if target == self.nums[ind]:
                return ind


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
