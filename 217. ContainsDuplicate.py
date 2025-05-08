"""
LeetCode Problem 217: Contains Duplicate
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/
Tags: Array, Hash Table

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, value in enumerate(nums):
            if value in seen: 
                return True
            seen[value] = i 
        return False

solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1])) # True
print(solution.containsDuplicate([1, 2, 3, 4])) # False