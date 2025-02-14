class Solution(object):
  def removeDuplicates(self, nums):
    left = 0  #left pointer for unique elements
    for right in range(1, len(nums)): #right pointer start from 1
      if nums[right] != nums[left]:
        left +=1
        nums[left] = nums[right]
      return left + 1
    
    #left pointer keep track the unique elements at position 0, by search right value from position 1, whenever a new uniqie element is fund, update left position +1, and value = right. The number of unique elements is the left pointer + 1