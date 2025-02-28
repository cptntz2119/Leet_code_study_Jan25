class Solution(object):
  def findKthMissingPositive(self, arr, k):
    #burtal force
    num = 1
    missing_count = 0
    i = 0
    while missing_count < k:
      if i < len(arr) and arr[i] == num:
        i +=1
      else:
        missing_count += 1
      
      if missing_count ==k:
        return num
      num +=1
    return -1
# Time complexity: O(n)
# Space complexity: O(1)
# This approach uses a brute-force method to find the kth missing positive number.
# The num variable is used to keep track of the current number being checked.
# The missing_count variable is used to keep track of the number of missing positive numbers found so far.
# The i variable is used to iterate through the input array.
# The while loop continues until the kth missing positive number is found.
# If the current number is found in the array, the i variable is incremented.
# Otherwise, the missing_count variable is incremented.
# If the kth missing positive number is found, it is returned.  