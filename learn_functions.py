# functions
def greet():
  name = input("Hello. Please enters your name:\n")
  print(f"Hello {name}")
  return name

# greet()

# arguments and params
car ={
    "make": "Ford"
  }
def calculate_mpg():
  c

# return is same as return None

# default parameters
def add(x, y = 4):
  return x + y

# calling using named arguments
total = add(x=55, y= 64)
t_delegate = total
print(t_delegate(5,6)) # first class functions
# lmbda
divide = lambda x, y : x / y
add_l = lambda x, y : x + y
print(add_l(50, 60))

print((lambda x, y: x + y)(60, 70))

