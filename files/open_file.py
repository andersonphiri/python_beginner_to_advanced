my_file = open('data.txt', 'r')

file_content = my_file.read()
my_file.close()
print(file_content)


# write to file
my_write_file = open('data.txt', 'w')
user_input = input('Enter your name:\n')
my_write_file.write(user_input)
my_write_file.close()