class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        chars = {"a" : 1, "e" : 2, "i" : 4, "o" : 8, "u" : 16}
        mp = [-2 for i in range(0, 32)]
        mp[0] = -1
        mask = 0
        longestsub = 0
        for i in range(0, len(s)) :
            if s[i] in chars.keys() :
                mask = mask ^ chars[s[i]]
            if mp[mask] == -2 :
                mp[mask] = i
            longestsub = max(longestsub, i - mp[mask])
        return longestsu