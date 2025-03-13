from collections import defaultdict, deque

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    #step1: build graph, where graph is a dictionary, key is the course, value is the list of courses that depend on the key course
    graph = defaultdict(list)
    for a, b in prerequisites:
      graph[a].append(b)
    #step2: build in-degrees, where in-degrees represets how many courses need to be taken before taking the course
    in_degrees = [0] *numCourses
    for a,b in prerequisites:
      in_degrees[a] +=1
    #step3: build queue, where queue is the course that has no prerequisites, mean in-degrees is 0
    queue = deque([i for i in range(numCourses) if in_degrees ==0])
    process_courses = 0
    #step4: start the course, and unlock the course that depend on this course, if in_degree is 0, add to queue
    while queue:
      course = queue.popleft()
      process_courser +=1 #whenever pop a course, mean done the course, so unlock the next course
      for next_course in graph[course]:
        in_degrees[next_course] -=1
        if in_degrees[next_course] ==0:
          queue.append(next_course)
    return process_courses == numCourses
  
# Time complexity: O(n)
# Space complexity: O(n)
# Test cases:
# 2, [[1,0]] => True
      
