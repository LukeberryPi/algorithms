# https://leetcode.com/problems/two-sum/description/

from typing import List

nums = [2, 3, 5, 7]
target = 10

def two_sum(nums: List[int], target: int):
    map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in map:
            return [map[diff], i]
        
        map[n] = i
    

print(two_sum(nums, target))
