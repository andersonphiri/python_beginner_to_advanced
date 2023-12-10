# imagine a tuple 
currencies = 9.9,45
eur,zim_dollar = currencies
print(f"{eur} is equivalent to {zim_dollar} zim dollars")

# now imagine a list of tuples 
friends = [("john", 55), ("Andrew", 23), ("Bob", 99)]

for friend in friends:
    name,age = friend
    print(f"{name} is {age} years old")