"""
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map = {k[0]: k[1] for k in knowledge}
        result = ""
        curr = ""
        i = 0
        while i < len(s):
            if s[i] != "(":
                result += s[i]
            else:
                i += 1
                while s[i] != ")":
                    curr += s[i]
                    i += 1
                if curr in knowledge_map:
                    result += knowledge_map[curr]
                else:
                    result += "?"
                curr = ""
            i += 1
        return result
