age = 30
edge = age//4
# here is a comment

# moduulus operator
remainder = 13 % 5;

# strings
my_string = "Helo, it' s me"
print(my_string)
multiline = """
Hello mr sir.

What up?

"""
print(multiline)

"""
multiline comments
"""

a_number = 23
a_number_as_string = str(a_number)
# string formatting using fstrings
print(f"You are {a_number} , years old")

# dynamic string formatting
name = "anderson"
greeting_template = "How are you, {}"
anderson_greeting = greeting_template.format(name)
print(anderson_greeting)

# another way to string template
greeting_template_2 = "I come from {country}"
come_from_zimbabwe = greeting_template_2.format(country="Zimbabwe")
print(come_from_zimbabwe)
country = "hong kong"
print(greeting_template_2.format(country=country))

# user input
your_age = float(input("Enter your age: "))
print(f"you have lived for {your_age * 12} months" ) # prints your_age value 12 times

# string index

