class Solution(object):
  def reverseString(self, s):
    left, right = 0, len(s)-1
    while left < right:
      s[left],s[right] = s[right],s[left]    
      left +=1
      right -=1
    return s
  
# test case:
s = ["h","e","l","l","o"]
sol = Solution()
print(sol.reverseString(s))