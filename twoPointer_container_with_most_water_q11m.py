class Solution(object):
  def maxArea(selft,height):
    left, right = 0, len(height) -1
    max_area = 0
    while left < right:
      area = (right - left) * min(height[left], height[right])
      max_area = max(max_area, area)
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    return max_area
#The two-pointer approach is used to find the maximum area between two vertical lines in the histogram
#The left and right pointers start at the beginning and end of the histogram
#The area between the two lines is calculated as the width (right - left) multiplied by the minimum height of the two lines
#The maximum area is updated if the current area is greater
#The pointer with the smaller height is moved towards the center to potentially find a larger area  
#The process continues until the left and right pointers meet
#The maximum area found is returned
#The time complexity of this solution is O(n), where n is the number of elements in the input array. The two-pointer approach iterates through the array once, updating the maximum area in each step. Thus, the time complexity is linear with respect to the input size.  
#The space complexity of this solution is O(1) since we are using a constant amount of extra space to store the pointers and the maximum area. The input array is not modified, and no additional data structures are used. 
