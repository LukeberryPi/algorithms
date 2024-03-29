# https://leetcode.com/problems/roman-to-integer/

roman = "MCMXCIV"

# recebemos uma string contendo apenas caracteres romanos válidos
# entre [I, V, X, L, C, D, M]
# retornar o equivalente em decimal

def roman_to_numeral(s: str) -> int:
    numeral = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    for i in range(len(s) - 1):
        curr, next = s[i], s[i + 1]
        
        if roman[curr] < roman[next]:
            numeral -= roman[curr]
        else:   
            numeral += roman[curr]

    return numeral + roman[s[-1]]


print(roman_to_numeral(roman))
