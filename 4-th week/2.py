"""
https://leetcode.com/problems/container-with-most-water/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxs = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxs = max(maxs, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxs
