EXERCISE_LINK = "https://leetcode.com/problems/roman-to-integer/"

roman = "MCMXCIV"

# recebemos uma string contendo apenas caracteres romanos válidos
# entre [I, V, X, L, C, D, M]
# retornar o equivalente em decimal

def roman_to_numeral(s: str) -> int:
    hashmap = {
      "I": 1,
      "IV": 4,
      "V": 5,
      "IX": 9,
      "X": 10,
      "XL": 40,
      "L": 50,
      "XC": 90,
      "C": 100,
      "CD": 400,
      "D": 500,
      "CM": 900,
      "M": 1000
    }
    
    numeral = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in hashmap:
            numeral += hashmap[s[i:i + 2]]
            i += 2
        else:
            numeral += hashmap[s[i]]
            i += 1

    return numeral


print(roman_to_numeral(roman))
