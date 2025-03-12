from collections import deque

class Solution (object):
  def orangesRotting(self, grid):
    if not grid:
      return 0
    
    queue =deque()
    fresh = 0
    rows, cols = len(grid), len(grid[0])

    #find all rotten oranges, and add to queue
    for r in range(rows):
      for c in range(cols):
        if grid[r][c]==2:
          queue.append((r,c))
        elif grid[r][c] ==1:
          fresh += 1
    if fresh == 0:
      return 0
    #start from rotten in the queue, and 4 directions and count time
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    minutes = 0
    while queue:
      size = len(queue)
      for _ in range(size): #each rotten orange in the queue
        row, col = queue.popleft()
        for dr, dc in directions: #for all 4 directions
          row_new, col_new = row + dr, col + dc
          if 0 <= row_new < rows and 0 <=col_new < cols and grid[row_new][col_new] ==1:
            grid[row_new][col_new] = 2
            fresh -= 1
            queue.append((row_new, col_new)) #add new rotten orange to the queue
      if queue:
        minutes += 1 #for each rotten in the queue, we add 1 minute, if queue is empty, we don't add 1 minute
    return minutes if fresh ==0 else -1
    #return -1 if not all oranges are rotten

# Time complexity: O(n)
# Space complexity: O(n)
