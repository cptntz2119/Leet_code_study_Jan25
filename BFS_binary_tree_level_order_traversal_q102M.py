
from collections import deque

class TreeNode:
  def __init__ (self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
class Solution(object):
  def levelOrder(self, root):
    if not root:
      return []
    
    queue = deque([(root,0)])
    result =[]

    while queue:
      node, depth = queue.popleft()
      #create result list of lists, the list should exist at the depth level, so should create early
      if(len(result) <= depth):
        result.append([])
      #access the root, and pop,still in that level, we append the value to the list
      result[depth].append(node.val)
      #add children to the queue of the same level, goin to while loop, just rinse and repeat
      if node.left:
        queue.append((node.left,depth+1))
      if node.right:
        queue.append((node.right, depth+1))
    return result
  
  #time complexity: O(n)
  #space complexity: O(n)
  