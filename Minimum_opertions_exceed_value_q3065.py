"""You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k. 
"""

class Solution(object):
  def minOperations(self, nums, k):
    count = 0

    while nums and min(nums) < k:
      nums.remove(min(nums))
      count += 1
    return count
  
# Time complexity: O(n^2), find min take O(n) and remove take O(n)
# Space complexity: O(1)

#optimized soulution will be using min-heap
import heapq
class Solution(object):
  def minOperations(self, nums, k):
    heap = []
    for num in nums:
      heapq.heappush(heap, num)
    
    count = 0
    while heap and heap[0] < k:
      heapq.heappop(heap)
      count += 1
    return count  
  
# Time complexity: O(nlogn), find min take O(logn) and remove take O(logn): 
# Heapify takes O(n).
#	Removing the smallest element takes O(log n).
#	If we remove n elements, total complexity is O(n log n).



  