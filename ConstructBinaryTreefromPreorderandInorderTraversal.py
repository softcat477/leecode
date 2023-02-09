# Definition for a binary tree node.
from typing import List, Tuple, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def construct(self, queue: deque, candy_left: List[int], candy_right: List[int], node: TreeNode) -> Tuple[deque, TreeNode]:
        if len(candy_left) != 0:
            # 1. Find the left child
            left = queue.popleft()
            # 2. Find the left-subtree of the left child, and the right-subtree of the left child
            left_idx = candy_left.index(left)
            candy_ll = candy_left[:left_idx]
            candy_lr = candy_left[left_idx + 1:]
            # 3. Create left child, attach to node
            node.left = TreeNode(left)
            # 4. Dive down if either its left-subtree or right-subtree != 0
            queue, _ = self.construct(queue, candy_ll, candy_lr, node.left)

        if len(candy_right) != 0:
            # Repeat 1~4 but do on the right child
            right = queue.popleft()
            right_idx = candy_right.index(right)
            candy_rl = candy_right[:right_idx]
            candy_rr = candy_right[right_idx + 1:]
            # 3. Create left child, attach to node
            node.right = TreeNode(right)
            # 4. Dive down if either its left-subtree or right-subtree != 0
            queue, _ = self.construct(queue, candy_rl, candy_rr, node.right)

        # return deque and node
        return queue, node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        queue = deque(preorder)
        root_val = queue.popleft()
        root = TreeNode(root_val)

        root_idx = inorder.index(root_val)
        candy_left = inorder[:root_idx]
        candy_right = inorder[root_idx + 1:]

        _, root = self.construct(queue, candy_left, candy_right, root)
        return root

def printTree(node):
    def rec(node, table, layer):
        if layer not in table:
            table[layer] = []
        if node != None:
            table[layer].append(node.val)
            table = rec(node.left, table, layer+1)
            table = rec(node.right, table, layer+1)
        else:
            table[layer].append("null")
        return table
    table = {}
    table = rec(node, table, 0)
    for key, item in table.items():
        print (f"{key} : {item}")

sol = Solution()

preo1 = [3,9,20,15,7]
ino1 = [9,3,15,20,7]

preo2 = [-1]
ino2 = [-1]

preo3 = [6,2,1,4,3,5,8,7,9]
ino3 = [1,2,3,4,5,6,7,8,9]

preo4 = [3,2,1]
ino4 = [1,2,3]

preo5 = [3,2,1]
ino5 = [3,2,1]

ans = sol.buildTree(preo1, ino1)
printTree(ans)

ans = sol.buildTree(preo2, ino2)
printTree(ans)

ans = sol.buildTree(preo3, ino3)
printTree(ans)

ans = sol.buildTree(preo4, ino4)
printTree(ans)

ans = sol.buildTree(preo5, ino5)
printTree(ans)
