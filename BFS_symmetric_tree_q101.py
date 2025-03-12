from collections import deque

class Solution(object):
  def isSymmetric(self, root):
    if not root:
      return True
    
    queue = deque([(root.left, root.right)])
#queue root's left and right children, start from there
    while queue:
      left, right = queue.popleft()
      #compare the first children, they should be same, only 2==2, if 2 and null, or null and 2, and 2 and 3 are not sysmetric
      if not left and not right:
        continue
      if not left or not right:
        return False
      if left.val != right.val:
        return False
      #then we append the left's left and right's right togethere,and do the comapre
      #apend the left's right and right's left together, and do the compare
      queue.append((left.left, right.right))
      queue.append((left.right, right.left))

      return True
# Time complexity: O(n)
# Space complexity: O(n)  
# The isSymmetric function takes a binary tree as input and returns True if the tree is symmetric, and False otherwise.
# The function first checks if the root is None and returns True if it is.
# The function then creates a deque called queue and adds the left and right children of the root to the queue.
# The while loop continues until the queue is empty.
# Inside the loop, the function dequeues the left and right nodes from the queue.
# If both nodes are None, the loop continues.   
