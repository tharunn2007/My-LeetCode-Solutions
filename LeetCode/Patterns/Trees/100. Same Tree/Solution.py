# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        result1 = []
        result2 =[]
        def traversep(node):
            if not node:
                return
            traversep(node.left)
            result1.append(node.val)  # Appends in-place to the same list
            traversep(node.right)
        traversep(p)
        
        def traverseq(node):
            if not node:
                return
            traverseq(node.left)
            result2.append(node.val)  # Appends in-place to the same list
            traverseq(node.right)
        traverseq(q)

        if result1 == result2:
            return True
        return False