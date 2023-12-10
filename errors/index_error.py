friends = ['john', 'rob']
print(friends[3]) # throws an index error

movies = {"name": 'moviename', "year": 2003}
print(f"Release year: {movies['years']}") # throws keyError 

friends_nearby = ['rob', 'pike']

inter = friends.intersection(friends_nearby) # throws an attribute error since intersection method applies to sets  and not lists

# not implemented error
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    

    def login(self):
        raise NotImplementedError('zhege feature buyou implemented! xiexie')
    

    def register(self):
        raise DeprecationWarning('hey, this method is deprecated..')
    

# value error:  raised by built in functions
parse = int('22.5') # the string being parsed is not int, it is float


