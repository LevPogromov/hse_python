"""
https://leetcode.com/problems/minimum-time-difference/
?envType=daily-question&envId=2024-09-16
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints :
            h = int(time[:2])
            m = int(time[3:])
            minute = h*60 + m
            minutes.append(minute)
        minutes.sort()
        ans = 99999
        for i in range(0, len(minutes)-1) :
            ans = min(ans, minutes[i+1] - minutes[i])
        return min(ans, 24*60 - minutes[len(minutes)-1] + minutes[0])