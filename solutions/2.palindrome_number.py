EXERCISE_LINK = "https://leetcode.com/problems/palindrome-number/"

num = 12121

# recebemos um número
# retornamos se esse número é palíndromo ou não
# 123 é palíndromo de 321

def palindrome_number(n):
    num_list = [x for x in str(num)]
    reversed = num_list[::-1]

    return num_list == reversed
    

print(palindrome_number(num))
