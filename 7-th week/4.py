"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        m = curr = sum(cardPoints[:size])
        for i in range(len(cardPoints) - size):
            curr += cardPoints[size + i] - cardPoints[i]
            m = min(m, curr)
        return sum(cardPoints) - m
