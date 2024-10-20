"""
https://leetcode.com/problems/bulls-and-cows/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        mp = {}
        for i in range(0, len(secret)):
            mp[secret[i]] = mp.get(secret[i], 0) + 1
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                if mp[secret[i]] == 0:
                    cows -= 1
                    mp[secret[i]] = 1
                mp[secret[i]] -= 1
                bulls += 1
            elif guess[i] in mp and mp[guess[i]] > 0:
                cows += 1
                mp[guess[i]] -= 1
        return str(bulls) + "A" + str(cows) + "B"
