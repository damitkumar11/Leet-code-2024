# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0

            # If the node value is within the range, include it in the sum
            if low <= node.val <= high:
                current_sum = node.val
            else:
                current_sum = 0

            # Recursively traverse left and right subtrees
            current_sum += dfs(node.left)
            current_sum += dfs(node.right)

            return current_sum

        return dfs(root)
        