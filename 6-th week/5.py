"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        mp1 = {}
        mp2 = {}
        for i in range(0, len(p)):
            mp1[s[i]] = mp1.get(s[i], 0) + 1
            mp2[p[i]] = mp2.get(p[i], 0) + 1
        if mp1 == mp2:
            ans.append(0)
        for i in range(len(p), len(s)):
            mp1[s[i]] = mp1.get(s[i], 0) + 1
            mp1[s[i - len(p)]] -= 1
            if mp1[s[i - len(p)]] == 0:
                del mp1[s[i - len(p)]]
            if mp1 == mp2:
                ans.append(i - len(p) + 1)
        return ans
