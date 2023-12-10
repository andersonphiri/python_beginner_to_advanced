class Car:
    def __init__(self, make, model) -> None:
        self.make= make 
        self.model = model


    def __repr__(self) -> str:
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self) -> None:
        self.cars = [];


    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'tried to add a `{car.__class__.__name__}` to the garage but you can only add Car')
        # raise NotImplementedError('we are unable to add new cars yet!')
        self.cars.append(car)


cars = Garage()

try:
    cars.add_car('toyota')

except TypeError:
    print('your car was not an error')

except AttributeError:
    pass

except Exception:
    raise

finally:
    pass




# run something if there is no exception 
try:
    cars.add_car('toyota')

except TypeError:
    print('your car was not an error')

else:
    print('this block will execute only if an exception doe not occur')