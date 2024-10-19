"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums):
      # nums = [1, 2, 3, 1]
      # O(n) time and O(n) space
      hm = {}
      for n in nums:
        if n in hm:
          return True
        hm[n] = True
      return False
    
    def containsDuplicateSet(self, nums):
      # nums = [1, 2, 3, 1]
      # O(n) time and O(n) space
      hm = set()
      for n in nums:
        if n in hm:
          return True
        hm.add(n)
      return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 4]))  # False
    print(solution.containsDuplicate([1, 2, 3, 1]))  # True
    print(solution.containsDuplicateSet([1, 2, 3, 4]))  # False
    print(solution.containsDuplicateSet([1, 2, 3, 1]))  # True