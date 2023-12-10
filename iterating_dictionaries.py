students_scores = {
    "stduent_one": 89,
    "student_two": 99,
    "stduent_three": 48
}
# to iterate keys only 
for key in students_scores:
    print(key)

print("\r\n")
# or 
for key in students_scores.keys():
    print(key)


# for values only

for val in students_scores.values():
    print(val)