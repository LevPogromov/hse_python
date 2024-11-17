"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        ans = 0
        max_cnt = 0
        letters = {}
        for j in range(0, len(s)):
            letters[s[j]] = letters.get(s[j], 0) + 1
            max_cnt = max(max_cnt, letters[s[j]])
            while j - i + 1 - max_cnt > k:
                letters[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
