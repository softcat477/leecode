from typing import Optional, List, Tuple
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recSolve(self, node:Optional[TreeNode], k:int) -> Tuple[bool, int]:
        if node == None:
            return False, 0

        found_left, left_child_count = self.recSolve(node.left, k)
        # Found
        if found_left:
            return True, left_child_count
        if left_child_count + 1 == k:
            return True, node.val

        # Search right
        found_right, right_child_count = self.recSolve(node.right, k - left_child_count - 1)
        if found_right:
            return True, right_child_count
        return False, left_child_count + right_child_count + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, ans = self.recSolve(root, k)
        return ans

sol = Solution()

tc1 = TreeNode(3)
tc1.left = TreeNode(1)
tc1.left.right = TreeNode(2)
tc1.right = TreeNode(4)
print (sol.kthSmallest(tc1, 1), 1)
print (sol.kthSmallest(tc1, 2), 2)
print (sol.kthSmallest(tc1, 3), 3)
print (sol.kthSmallest(tc1, 4), 4)

tc2 = TreeNode(5)
tc2.left = TreeNode(3)
tc2.left.left = TreeNode(2)
tc2.left.left.left = TreeNode(1)
tc2.left.right = TreeNode(4)
tc2.right = TreeNode(6)

print (sol.kthSmallest(tc2, 1), 1)
print (sol.kthSmallest(tc2, 2), 2)
print (sol.kthSmallest(tc2, 3), 3)
print (sol.kthSmallest(tc2, 4), 4)
print (sol.kthSmallest(tc2, 5), 5)
print (sol.kthSmallest(tc2, 6), 6)

tc3 = TreeNode(5)
print (sol.kthSmallest(tc3, 1), 5)

tc4 = TreeNode(5)
tc4.left = TreeNode(4)
tc4.left.left = TreeNode(3)
tc4.left.left.left = TreeNode(2)
tc4.left.left.left.left = TreeNode(1)
print (sol.kthSmallest(tc4, 1), 1)
print (sol.kthSmallest(tc4, 2), 2)
print (sol.kthSmallest(tc4, 3), 3)
print (sol.kthSmallest(tc4, 4), 4)
print (sol.kthSmallest(tc4, 5), 5)

tc4 = TreeNode(1)
tc4.right = TreeNode(2)
tc4.right.right = TreeNode(3)
tc4.right.right.right = TreeNode(4)
tc4.right.right.right.right = TreeNode(5)
print (sol.kthSmallest(tc4, 1), 1)
print (sol.kthSmallest(tc4, 2), 2)
print (sol.kthSmallest(tc4, 3), 3)
print (sol.kthSmallest(tc4, 4), 4)
print (sol.kthSmallest(tc4, 5), 5)
