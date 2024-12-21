"""
https://leetcode.com/problems/unique-binary-search-trees/description/
?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def numTrees(self, n: int) -> int:
        tree = [1] * (n + 1)
        for i in range(2, n + 1):
            curr = 0
            for j in range(1, i + 1):
                curr += tree[j - 1] * tree[i - j]
            tree[i] = curr
        return tree[n]
