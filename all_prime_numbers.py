#print all prime numbers
for n in range(2, 11):
  for x in range(2, n):
    if (n%x == 0):
      print(f"{n} = {x} * {n // x}")
  else:
    print(f"{n} is a prime number")