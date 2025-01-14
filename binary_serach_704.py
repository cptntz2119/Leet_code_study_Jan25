class Solution(object):
  def search(self, nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
      mid = (left + right) //2
      if target < nums[mid]:
        right = mid - 1
      elif target > nums[mid]:
        left = mid + 1
      else:
        return mid
    return -1
  
  #add test case
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.search(nums, target))  # Expected output: 4

    target = 2
    print(solution.search(nums, target))  # Expected output: -1

    nums = [1, 3, 5, 7]
    target = 5
    print(solution.search(nums, target))  # Expected output: 2
