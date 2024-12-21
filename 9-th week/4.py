"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
?envType=problem-list-v2&envId=binary-tree
"""


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convertToArray(head):
            arr = []
            while head != null:
                arr.append(head.val)
                head = head.next
            return arr

        def dfs(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        arr = convertToArray(head)
        return dfs(0, len(arr) - 1)
