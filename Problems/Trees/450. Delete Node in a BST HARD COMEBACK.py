# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right , key)
        elif key < root.val:
            root.left = self.deleteNode(root.left , key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                root = self.deleteNode(root.right, key)
            elif root.right is None:
                root = self.deleteNode(root.left, key)
            else:
                minNode = self.minNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
    
    def minNode(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr