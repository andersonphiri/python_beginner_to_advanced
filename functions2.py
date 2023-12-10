cars = [
    {"make": "isuzu", "model": "BT", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350}
]
def compute_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car=car)
    mpg = compute_mpg(car=car)
    print(f"{name} does {mpg} miles per gallon")

for car in cars:
    print_car_info(car=car)


# named arguments and f
print(1,2,3,4,5, sep="--")

# lambdas functions
divide_lambda = lambda x,y,z : z + (x / y)
# self executing lambda, like in javascript 
print((lambda x,y,z : z + (x/y))(10,20,30)) # but do not do this, as this is not readable


# first class, higher order functions 
def before_and_after(func):
    print("his is before...")
    func()
    print("this is after")

def delegate():
    print("this is in between")

before_and_after(delegate)


# more interesting thangs
ops = {
    "avg": lambda seq : sum(seq) / len(seq),
    "total": lambda seq : sum(seq),
    "top": lambda seq : max(seq)
}
ops_alternative = {
    "avg": lambda seq : sum(seq) / len(seq),
    "total":  sum,
    "top":  max,
    "info": print_car_info

}
