# method -2 
def make_car(manufacturer, model, **features):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(features)
    return car

if __name__ == "__main__":
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)