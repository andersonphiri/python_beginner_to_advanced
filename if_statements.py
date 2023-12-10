# if else
user = "anderson"
if user == input("Enter username \n"):
  print("yes")
else:
  print("hellow stranger")

print(bool(-1))

arr = [1,2,3,4,5,6,7,8]
# swap 2 and 6
arr[2],arr[6] = arr[6], arr[2]
print(arr)

if 9 in arr:
  print('yes. 9 is in the list')
elif 3 in arr:
  print('oohsome 3 found')
else:
  print('naaah')
