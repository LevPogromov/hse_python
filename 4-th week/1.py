"""
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
?envType=daily-question&envId=2024-10-12
"""


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_time = sorted(i[0] for i in intervals)
        end_time = sorted(i[1] for i in intervals)
        cnt, j = 0, 0
        for start in start_time:
            if start > end_time[j]:
                j += 1
            else:
                cnt += 1
        return cnt
