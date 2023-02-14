EXERCISE_LINK = "https://leetcode.com/problems/palindrome-number/"

num = 101

# recebemos um número
# retornamos se esse número é palíndromo ou não
# 123 é um palíndromo de 321

def palindrome_number(x):
    if x < 0 or str(x)[-1] == 0:
        return False
    
    num_list = [ch for ch in str(x)]
    reversed = num_list[::-1]

    return reversed == num_list


print(palindrome_number(num))
