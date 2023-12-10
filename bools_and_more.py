truth = True
age = 29
is_over_age = age >= 41
 #string 
name = str("anderson")
print(name)

# and or operators
can_try = age == 45 and age % 2 == 1 or age % 5 == 0


# bool fn
print(bool(35))
print(bool(0.0))
print(bool("anderson"))
print(bool(""))

## 
surname = "Phiri"
greeting = "" or f"Mr {surname}"
print(greeting)
print(f"Not true is: {not True}")
print(f"Not false is: {not bool('')}")