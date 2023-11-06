from car_factory import CarFactory
from datetime import datetime

car = CarFactory.create_calliope(datetime(2022, 1, 1), 30501, 500)
print(car.needs_service())