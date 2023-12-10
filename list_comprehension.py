# list slice
frnds = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(frnds[:-2]) # excludes las two
print(frnds[1:4]) # from index one but not including index 4
print(frnds[-1:])

# list comprehension
nums = [0, 1, 2, 3, 4, 5, 6]
duble_nums = [num * 2 for num in nums]
print(duble_nums)
print(2**3)
friends_upper = [friend.lower() for friend in frnds]
# title casing
print(frnds[0].title())

# list comprehension with conditionals
ages = [23, 44, 75, 21, 29, 32]
odds = [age for age in ages if age % 2 == 1]
mf = ["rulf", "Ruth", "Charlie", "Jen", "LiberTY"]
guests = ["ruth", "jen"]
# set comprehension
mf_lower = set([m.lower() for m in mf 
                if len(m) > 3
                ])
guests_lower = set([g.lower() for g in guests])
print(guests_lower.intersection(mf_lower))

# dictionary comprehension
fs = ["anna", "ben", "chomsky"]
time_since_seen = [3, 9, 21]

lt_map = {
  fs[i]: time_since_seen[i]
  for i in range(len(fs))
  if time_since_seen[i] > 4
}

# the zip function
lt_map2 = dict(zip(fs, time_since_seen))