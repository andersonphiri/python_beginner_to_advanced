# a list
friends = ["andy", "john", "bob"]
friends.a
for i in range(0, 3):
  print(friends[i])

two_d_array = [["john", 38], ["andy", 29] ]
two_d_array.append(["fatso", 66])
for j in range(0, 3):
  for k in range(0, 2, 2):
    print(f"My name is {two_d_array[j][k] } and I am {two_d_array[j][  + 1] } years old")

# a tuple
short_tuple = "and", "phiri"
a_clearer_tuple = ("item 1", "item 2")
a_clearer_tuple += ("item 3",)
print(a_clearer_tuple)

# sets
my_set = {"cup", "port", "cup"}
my_set.add("teaport")
print(my_set)
my_set.remove("cup")

# sets operations
science = {"jack", "jackson", "son", "phil"}
arts = {"jsckson", "phil", "listen", "daren"}
arts_not_in_science = arts.difference(science)
not_in_both = arts.symmetric_difference(science)
print(arts_not_in_science)
# intersection
common = science.intersection(arts)

# dictionaries
friend_ages = {"Rulf": 23, "John" : 37, "Talus" : 48}
print(friend_ages["Talus"])
friends = (
  {"name": "aname1" , "age": 45},
  {"name": "aname 2" , "age": 4},
  {"name": "aname 3" , "age": 54}
)
print(friends[1]["name"])
friends_tuple = [("abidjan", 24), ("djakarta", 23), ("riley", 34)]
friends_dictionary = dict(friends_tuple)
print(friends_dictionary)
print(f"Dictionary has size: {len(friends_dictionary)}")

# length and sum
grades = [20, 40, 60]
print(f"total of : {sum(grades)}")

# joining a list
comma_separated = ", ".join(grades)


# list slice
frnds = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(frnds[:-2]) # las two
print(frnds[1:4]) # from index one but not including index 4
