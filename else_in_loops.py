# while loops: 

is_learning = False
while is_learning:
  print("You are leraning")
  is_learning = input("do you still learn: \n") == "yes"
else:
  print("no break encountered")


friends = ["mark", "mike", "jane"]
count = 1;
for _ in friends:
  print(count)
  count += 1

students = [
  {"name": "michael", "grade": 34},
  {"name": "david", "grade": 54}
]

for student in students:
  print(f'student {student["name"]} has a grade of {student["grade"]}')
else:
  print("no break encoun")