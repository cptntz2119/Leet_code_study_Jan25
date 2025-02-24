class Solution(object):
  def sortedSquares(self,nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n-1,-1,-1): #start from the end of the array, start at n-1, end at -1(stop at 0), step -1
      if abs(nums[left]) > abs(nums[right]):
        result[i] = nums[left] * nums[left]
        left += 1
      else:
        result[i] = nums[right] * nums[right]
        right -= 1
    return result 
  
#The two-pointer approach is used to find the squares of the sorted array elements. is better approach that return sorted(x*x for x in nums)
#The left and right pointers start at the beginning and end of the array  
#time complexity is O(n) because the two-pointer approach iterates through the array once, updating the squares of the elements in each step. Thus, the time complexity is linear with respect to the input size, sorted appraoch is O(nlogn)
#The space complexity of this solution is O(n) since we are using a new array to store the squares of the elements. The input array is not modified, and no additional data structures are used. the sorted approach is O(n) because it returns a new array

