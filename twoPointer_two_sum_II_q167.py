class Solution(object):
  def twoSum(selt, numbers, target):
    left, right = 0, len(numbers) -1
    while left < right:
      s = numbers[left] + numbers[right]
      if s == target:
        return[left+1, right+1] #asked to return 1-indexed array
      elif s < target:
        left += 1
      else:
        right -= 1
    return None

# The two-pointer technique is used to solve the problem, where the left and right pointers are initialized to the start and end of the array, respectively.  
# The sum of the elements at the left and right pointers is calculated.
# If the sum is equal to the target, return the indices of the left and right pointers.
# If the sum is less than the target, increment the left pointer.
# If the sum is greater than the target, decrement the right pointer.
# If no solution is found, return None.


# Time complexity: O(n)
# Space complexity: O(1)