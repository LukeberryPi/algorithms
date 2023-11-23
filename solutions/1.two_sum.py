# https://leetcode.com/problems/two-sum/description/

from typing import List

nums = [2, 3, 5, 7]
target = 10

# recebemos uma lista números e um número alvo
# temos que retornar os índices dos dois valores que somados são iguais ao nosso alvo
# no exemplo, são os valores 3 e 7, de índices 1 e 3

def two_sum(nums: List[int], target: int) -> List[int]:
    map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in map:
            return [map[diff], i]
        
        map[n] = i
    
    # unreachable return to satisfy type
    return [0, 0]
    

print(two_sum(nums, target))
