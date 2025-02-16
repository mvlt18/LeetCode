"""
Leetcode: 1. Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/
Tags: Array, Hash Table

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store the index of the elements already visited
        map = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in map:
                # return [index of the difference, current index]
                return [map[difference], index]
            # store the index of the value  
            map[value] = index


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print (solution.twoSum([3, 2, 4], 6))  # [1, 2]