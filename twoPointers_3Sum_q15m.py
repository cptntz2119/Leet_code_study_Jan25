class Soultion(object):
  def threeSum(self, nums):

    nums.sort()
    result = []

    for i in range(len(nums)-2):
      if i > 0 and nums[i] ==nums[i-1]:
        continue

      left,right = i+1, len(nums) - 1
      while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
          result.append([nums[i], nums[left], nums[right]])

          while left < right and nums[left] == nums[left +1]:
            left +=1
          while left < right and nums[right] == nums[right -1]:
            right -=1
        
          left +=1
          right -=1
        elif total < 0:
          left +=1
        else:
          right -=1
    return result
#The input array is sorted in ascending order
#The outer loop iterates through the array from the first element to the third-to-last element
#The inner loop uses two pointers, left and right, to find the two other elements that sum up to the target value
#The left pointer starts from the element after the current element, and the right pointer starts from the last element
#If the sum of the three elements is equal to the target value, we add the triplet to the result
#We then skip over any duplicate elements for the left and right pointers
#If the sum is less than the target value, we move the left pointer to the right
#If the sum is greater than the target value, we move the right pointer to the left
#We continue this process until the left pointer is less than the right pointer
#Finally, we return the list of triplets that sum up to the target value
#The time complexity of this solution is O(n^2), where n is the number of elements in the input array. The sorting step takes O(nlogn) time, and the two-pointer approach takes O(n) time. Thus, the overall time complexity is dominated by the sorting step, resulting in O(n^2) time complexity.
#The space complexity of this solution is O(1) since we are using a constant amount of extra space to store the result and the pointers. The input array is modified in place, so no additional space is required.
#The solution is efficient and does not require any additional data structures. It uses a two-pointer approach to find the triplets that sum up to the target value, taking advantage of the sorted nature of the input array. The solution avoids duplicate triplets by skipping over duplicate elements in the inner loop. Overall, the solution is concise and effective in finding the desired triplets.