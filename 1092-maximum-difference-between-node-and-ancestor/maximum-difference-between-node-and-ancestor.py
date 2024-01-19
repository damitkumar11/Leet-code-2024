# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val
            
            # Update min and max values on the current path
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            
            # Recursively traverse left and right subtrees
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)
            
            # Return the maximum difference encountered so far
            return max(left_diff, right_diff)
        
        # Start the DFS traversal from the root with initial min and max values
        return dfs(root, root.val, root.val)

# Example usage:
# Construct the binary tree from the given input
# root = TreeNode(8)
# root.left = TreeNode(3)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(4)
# root.left.right.right = TreeNode(7)
# root.right.right = TreeNode(14)
# root.right.right.left = TreeNode(13)

# Create an instance of the Solution class
# solution = Solution()

# Call the maxAncestorDiff method to find the maximum ancestor difference
# result = solution.maxAncestorDiff(root)

# Print the result
# print(result)
