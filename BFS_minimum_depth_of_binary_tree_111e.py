from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
  def minDepth(self, root):
    if not root:
      return 0
    
    queue = deque([(root,1)])
    while queue:
      node, depth = queue.popleft()

      if not node.left and not node.right:
        return depth
      if node.left:
        queue.append((node.left, depth+1))
      if node.right:
        queue.append((node.right, depth+1))
    return -1
# Time complexity: O(n)
# Space complexity: O(n)

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)

sol = Solution()
print(sol.minDepth(root))  # Output: 5
