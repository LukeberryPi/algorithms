a = [5, 4, -2, 3, 2, 4, 4, 4]

# hashmap
def compute_closest_to_zero(ts):
    if (len(ts) == 0):
        return 0

    if (0 in ts):
        return 0

    hash = {}

    for t in ts:
      if t not in hash:
        hash[t] = abs(t)

    for k, v in hash.items():
      if k and -k in hash.keys() and v == min(hash.values()):
        return abs(k)

      if v == min(hash.values()):
        return k


print("result:", compute_closest_to_zero(a))
