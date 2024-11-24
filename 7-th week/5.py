"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        mx = 0
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        mx = curr
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            mx = max(mx, curr)
        return mx
