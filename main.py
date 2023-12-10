# an dict of funcs
ops = {
  "avg" : lambda seq : sum(seq) / len(seq),
  "total" : sum ,#lambda seq : sum(seq),
  "top": max, #lambda seq : max(seq)
}
studs = [
  {"name": "Ay", "grades" : (67, 90, 95, 100) },
  {"name": "Bob", "grades": (56, 78, 80, 90)},
  {"name": "anderson", "grades": (98, 90, 95, 99)}
  
]

for stud in studs:
  name = stud["name"]
  total = ops["total"](stud["grades"])
  average = ops["avg"](stud["grades"])
  top = ops["top"](stud["grades"])
  print(f'name: {name}, total: {total}, averge: {average}, Max: {top}')