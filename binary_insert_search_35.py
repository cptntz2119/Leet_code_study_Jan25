class Solution:
  def searchInsert (self, nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
      mid = (left+right)//2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return left
  
# test
if __name__ == "__main__":
  solution = Solution()
  nums = [1,3,5,6]
  target = 5
  print(solution.searchInsert(nums, target))  # Expected output: 2

  nums = [1,3,5,6]    
  target = 2
  print(solution.searchInsert(nums, target))  # Expected output: 1

  nums = [1,3,5,6]
  target = 7
  print(solution.searchInsert(nums, target))  # Expected output: 4