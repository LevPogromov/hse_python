"""
https://leetcode.com/problems/3sum-closest/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dif = 9999999
        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(min_dif - target):
                    min_dif = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s
        return min_dif
