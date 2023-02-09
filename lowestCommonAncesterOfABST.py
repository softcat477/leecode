# Definition for a binary tree node.
from typing import Optional, Tuple
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recSolve(self, node: TreeNode, p: TreeNode, q:TreeNode) -> Tuple[bool, Optional[TreeNode]]:
        if node == None:
            return False, None

        if node.val == p.val or node.val == q.val:
            # One of p/q is the node
            l_found, _ = self.recSolve(node.left, p, q)
            r_found, _ = self.recSolve(node.right, p, q)

            # Found the other one in its child
            if l_found or r_found:
                return True, node
            else:
                # we say that we've found one of p/q but haven't found the LCA yet
                return True, None
        else:
            # Test if the l/r subtree contains p/q
            l_found, l_lca = self.recSolve(node.left, p, q)
            r_found, r_lca = self.recSolve(node.right, p, q)
            # p/q are all in one side
            if l_lca != None:
                return True, l_lca
            elif r_lca != None:
                return True, r_lca
            elif l_found and r_found:
                # p in one side, q in the other side
                return True, node
            else:
                # Not found
                return l_found or r_found, None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, ans = self.recSolve(root, p, q)
        return ans

sol = Solution()

tc = TreeNode(6)
tc.left = TreeNode(2)
tc.left.left = TreeNode(0)
tc.left.right = TreeNode(4)
tc.left.right.left = TreeNode(3)
tc.left.right.right = TreeNode(5)
tc.right = TreeNode(8)
tc.right.left = TreeNode(7)
tc.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(8)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 6)

p = TreeNode(2)
q = TreeNode(5)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 2)

p = TreeNode(2)
q = TreeNode(4)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 2)

p = TreeNode(2)
q = TreeNode(5)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 2)

p = TreeNode(6)
q = TreeNode(0)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 6)

p = TreeNode(3)
q = TreeNode(5)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 4)

tc = TreeNode(2)
tc.left = TreeNode(1)
p = TreeNode(2)
q = TreeNode(1)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 2)

p = TreeNode(1)
q = TreeNode(2)
ans = sol.lowestCommonAncestor(tc, p, q)
print (ans.val, 2)
