"""
https://leetcode.com/problems/word-break/description/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(0, len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and dp[start] and s[start : start + len(word)] == word:
                    dp[i] = True
                    break
        return dp[len(dp) - 1]
