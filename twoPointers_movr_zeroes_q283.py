class Solution(object):
  def moveZeroes(self, nums):
    left = 0  #left pointer is used to keep track of the position of the next non-zero element
    for right in range(len(nums)):
      if nums[right] != 0: #if nums[right] ==0, do nothing, right pointer will move to the next element until find the next non-zero element
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
    return nums
  
  #right pointer is used to iterate through the array
  #left pointer is used to keep track of the position of the next non-zero element
  #When a non-zero element is found, it is swapped with the element at the left pointer
  #The left pointer is then incremented by 1
  
