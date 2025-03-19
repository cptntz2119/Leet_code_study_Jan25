from collections import deque
from xml.dom import Node


class Solution(object):
  def cloneGraph(self, node):
    #1 graph is already provided, {1: [2,4], 2: [1,3], 3: [2,4], 4: [1,3]} with key = node, value = edges
    #2 build the clone, start with node
    #3 build a queue, start with node and make the clones, and add edges for the clones and update queue
    #4 return the clone
    if not node:
      return None #check empty graph
    #step 1
    clones = {node: Node(node.val)}
    queue = deque([node])
    #step 2, 3, 4
    while queue:
      current = queue.popleft() 
      #start with node,and add edges and add to queue
      for neighbor in current.neighbors:
        if neighbor not in clones:
          clones[neighbor] = Node(neighbor.val) #create clones with an instance of Node class
          queue.append(neighbor)
        
        clones[current].neighbors.append(clones[neighbor])
    return clones[node]
# Time complexity: O(n)
# Space complexity: O(n)
