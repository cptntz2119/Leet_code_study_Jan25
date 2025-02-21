class Solution(object):
  def minSubArrayLen(self, target, nums):
    left = 0
    min_len = float('inf')
    sum_val = 0

    for right in range(len(nums)):
      sum_val += nums[right]
      while sum_val >= target:
        min_len = min(min_len, right-left + 1)
        sum_val -= nums[left]
        left += 1 #update left after min_len and sum_val are updated
    return min_len if min_len != float('inf') else 0
  #time complexity is O(n) not O(n^2) enven when there is nested while loop, because the inner while loop is not reseted everytime, only updated with condition sum_val >= target, worst case is runing through the array twice, so it is O(2n) = O(n)
  #space complexity is O(1) because only a few extra variables are used, no additional data structures are used
  