import making_cars
from making_cars import make_car
from making_cars import make_car as mcar
import making_cars as mc
from making_cars import *

car = making_cars.make_car('subaru', 'outback', color='blue', tow_package=True)
car = make_car('subaru', 'outback', color='blue', tow_package=True)
car = mcar('subaru', 'outback', color='blue', tow_package=True)
car = mc.make_car('subaru', 'outback', color='blue', tow_package=True)
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)

