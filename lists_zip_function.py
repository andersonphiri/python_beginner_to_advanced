friends = ["and", "joe", "truant"]
time_since_seen = [3,6,8]

# ineficient: using comprehension 
long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
}
print(long_timers)

# efficient
print('efficient')
print(dict(zip(friends, time_since_seen)))

# if we convert the zip into lists, it will create a tuple
# zip will ignore extra element and only matches the 