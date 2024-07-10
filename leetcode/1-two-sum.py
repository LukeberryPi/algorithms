nums = [1, 3, 4, 5, 7]
target = 9

# you're given a list of integers nums and a target integer target.
# return the index of the first two elements a, b in nums such that a + b == target
# assume there are always two numbers that satisfy this requisite

# nums = [4, 6, 8, 10]
# target = 14

# for each number
# find the difference between the target and that number
# eg
# 4 -> diff 5
# if the diff already exists,
# store in a hash as num : i

def two_sum(nums, target):
    hash = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff not in hash:
            hash[num] = i

        if diff in hash:
            return [hash[diff], i]

    return None

print("result:", two_sum(nums, target))
