"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        mp = {}
        i = 0
        max_len = 0
        for j in range(0, len(s)):
            mp[s[j]] = mp.get(s[j], 0) + 1
            if len(mp) == j - i + 1:
                max_len = max(max_len, j - i + 1)
            else:
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    mp.pop(s[i])
                i += 1
        return max_len
