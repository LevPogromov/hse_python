"""
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
?envType=daily-question&envId=2024-10-04
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        ans = 0
        last = skill[0] + skill[-1]
        while i < j:
            if skill[i] + skill[j] == last:
                ans += skill[i] * skill[j]
                last = skill[i] + skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return ans
