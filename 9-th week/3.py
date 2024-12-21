"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        flag = False
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                level.reverse()
            ans.append(level)
            flag = not flag
        return ans
