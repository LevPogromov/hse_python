"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        mp = {}
        for j in range(0, len(s)):
            mp[s[j]] = 1 + mp.get(s[j], 0)
            while mp[s[j]] > 1:
                mp[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
