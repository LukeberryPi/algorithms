from typing import List

EXERCISE_LINK = "https://leetcode.com/problems/longest-common-prefix/"

strs = ["flower", "flow", "flight"]

# recebemos uma lista de strings em lowercase
# devemos retornar qual o "maior" prefixo elas tem em comum
# ["cachorro", "carro", "cabeça"] => maior prefixo é "ca"

def longest_prefix(strs: List[str]) -> str:
    result = ""
    sort = sorted(strs)

    first, last = sort[0], sort[-1]

    for char_f, char_l in zip(first, last):
        if char_f != char_l:
            break
        result += char_f

    return result


print(longest_prefix(strs))
