class Solution(object):
  def twoSum(self, nums, target):
    tempMap = {}
    for i, n in enumerate(nums):
      if target - n in tempMap:
        return[tempMap[target-n],i]
      tempMap[n] = i

# Time complexity: O(n)
# Space complexity: O(n)
#haspmap is used to store the index of the element in the array, where n is the value and i is the index using enumerate function.{n:i}
#If the difference between the target and the current element is in the hashmap, return the index of the difference and the current index.
#If the difference is not in the hashmap, add the current element to the hashmap.
#If no solution is found, return None.

