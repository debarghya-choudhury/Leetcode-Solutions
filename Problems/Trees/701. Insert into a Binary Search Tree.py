# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        valNode = TreeNode(val)
        p1 = dummy = TreeNode()
        dummy.right = root

        while root:
            p1 = root
            if val > root.val:
                root = root.right
            else:
                root = root.left

        if p1 and val > p1.val:
            p1.right = valNode
        else:
            p1.left = valNode
        
        return dummy.right

