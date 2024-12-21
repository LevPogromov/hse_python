"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        lvl = [root]
        while root and lvl:
            ans.append([node.val for node in lvl])
            lvl = [
                child
                for parent in lvl
                for child in (parent.left, parent.right)
                if child
            ]
        return ans
