class Solution(object):
  def isPalindrome(self, s):
    left, right = 0, len(s) - 1
    cleaned_s = []
    for c in s:
      if c.isalnum():
        cleaned_s.append(c.lower())
    s = ''.join(cleaned_s)
    while left <= right:
      if s[left] == s[right]:
        left += 1
        right -= 1
      else:
        return False
    return True
  

# Time complexity: O(n)
# Space complexity: O(n)
# The two-pointer technique is used to solve the problem, where the left and right pointers are initialized to the start and end of the string, respectively.
# The string is first cleaned by removing non-alphanumeric characters and converting all characters to lowercase.
# The characters at the left and right pointers are compared.
# If the characters are equal, the left pointer is incremented and the right pointer is decremented.
# If the characters are not equal, return False.
# If the pointers cross each other, return True.
# If no solution is found, return False.

