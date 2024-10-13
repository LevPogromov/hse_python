"""
https://leetcode.com/problems/3sum/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        print(nums)
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    arr.append((nums[i], nums[j], nums[k]))
                    j += 1
        return set(arr)
