from collections import defaultdict, deque


class Solution(object):
  def countComponents(self, n, edges):
    #1 build the graph
    graph = defaultdict(list) #create empty graph so that we can add edges, it won't throw error like key not found
    for a,b in edges:
      graph[a].append[b]
      graph[b].append[a]
    #undirected graph, a <->b both ways
    #step 2, create visited set, using set becasue set only store unique vlues
    visited = set()
    #step3, create queue and start from node 0
    count = 0
    #step 4, start BFS
    def bfs(node):
      queue = deque([node])
      visited.add(node)
      #coponent =[]
      while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            #component.append(neighbor)
      return 1 #if want to print connected components do not return 1, should add a new component array and append each new component in it
      #print(f"Connected Component {count + 1}: {component}")
    #step 5, iterate over all nodes
    for node in range(n):
      if node not in visited:
        bfs(node)
        count +=1
    return count
# Time complexity: O(n) for BFS traversal
# Space complexity: O(n) for graph  + O(n) for visited set + O(n) for queue = O(n)

