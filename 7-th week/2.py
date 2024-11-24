"""
https://leetcode.com/problems/grumpy-bookstore-owner/submissions/1461848273/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        without_using_minutes = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                without_using_minutes += customers[i]
        curr = 0
        res_for_minutes = 0
        for i in range(minutes):
            if grumpy[i] == 1 and i < len(customers):
                curr += customers[i]
        res_for_minutes = curr
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                curr += customers[i]
            if grumpy[i - minutes] == 1:
                curr -= customers[i - minutes]
            res_for_minutes = max(res_for_minutes, curr)
        return without_using_minutes + res_for_minutes
