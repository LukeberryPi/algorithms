# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
ar = [1, 3, 5, 7, 10]

def canMakeArithmeticProgression(arr):
    sort = sorted(arr)
    first_diff = sort[1] - sort[0]

    for i, n in enumerate(sort[:-1:]):
        diff = sort[i + 1] - n

        if diff != None and diff != first_diff:
            return False

    return True


print(canMakeArithmeticProgression(ar))