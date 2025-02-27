class Solution(object):
  def threeSumClosest(self, nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    for i in range(n-2):
      l, r = i+1, n-1
      while l< r:
        total = nums[i] + nums[l] + nums[r]
        if abs(total - target) < abs(closest_sum - target):
          closest_sum = total
        if total == target:
          return total
        elif total < target:
          l +=1
        else:
          r -=1   
    return closest_sum

# Time complexity: O(n^2)
# Space complexity: O(1)
# This approach is similar to the 3Sum problem, with an extra step to keep track of the closest sum to the target value.
# The outer loop iterates through the array from the first element to the third-to-last element.
# The two-pointer approach is used to find the two other elements that sum up to the target value.
# The closest_sum variable is updated whenever a closer sum is found.
# The function returns the closest_sum value at the end.
