"""
https://leetcode.com/problems/count-and-say/description/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = "1"
        for i in range(2, n + 1):
            ans += "*"
            step = ""
            cnt = 1
            for j in range(1, len(ans)):
                prev = ans[j - 1]
                if ans[j] == prev:
                    cnt += 1
                else:
                    step += str(cnt) + prev
                    cnt = 1
            ans = step
        return ans
