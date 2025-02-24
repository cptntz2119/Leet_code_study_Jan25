class Solution(object):
  def fourSum(self,nums,target):
    result = []
    nums.sort()
    n = len(nums)

    for i in range(n-3):
      if i>0 and nums[i] == nums[i-1]:
        continue #skip duplicates at i
      #early termination for efficiency
      if nums[i]*4 >target:
        break #if the smallest sum is greater than target, break
      if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
        continue #if the largest sum is less than target, continue
      for j in range(i+1, n-2):
        if j>i+1 and nums[j] == nums[j-1]:
          continue

        left,right = j+1, n-1
        while left <right:
          total = nums[i] + nums[j] +nums[left] + nums[right]
          if total == target:
            result.append([nums[i], nums[j], nums[left], nums[right]])
            while left < right and nums[left] == nums[left+1]:
              left +=1
            while left < right and nums[right] == nums[right-1]:
              right -=1
            left +=1
            right -=1
          elif total < target:
            left +=1
          else:
            right -=1
    return result
  
# Time complexity: O(n^3)
# Space complexity: O(1)
# this approach is set left and right pointers on 3rd and 4th number and move them to find the sum of 4 numbers equal to target value 
# The outer loop iterates through the array from the first element to the fourth-to-last element    
# The inner loop iterates through the array from the second element to the third-to-last element
# The two-pointer approach is used to find the two other elements that sum up to the target value
